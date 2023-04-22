import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay,
    roc_auc_score,
)

sns.set_style("whitegrid")
sns.set_context("notebook")

X_train = None
X_test = None
y_train = None
y_test = None

TRAIN_RESULT_CSV_NAME = "train_results.csv"
TEST_RESULT_CSV_NAME = "test_results.csv"


def cm_to_metrics(cm):
    """ "Calculate accuracy, precision, recall and f1 score from confusion matrix.

    Parameters
    ----------
    cm : numpy.ndarray
        Confusion matrix.

    Returns
    -------
    tuple : (accuracy, precision, recall, f1)
        Tuple containing accuracy, precision, recall and f1 score.

    Examples
    --------
    >>> cm = np.array([[1, 0], [0, 1]])
    >>> cm_to_metrics(cm)
    (0.5, [0.5, 0.5], [0.5, 0.5], [0.5, 0.5])

    Notes
    -----
    The confusion matrix must be of shape (n_classes, n_classes) and
    contain only integers.

    References
    ----------
    [1] https://en.wikipedia.org/wiki/Confusion_matrix

    """
    tn, fp, fn, tp = cm.ravel()
    fp, fn, tp = cm.ravel()
    accuracy = (tn + tp) / cm.sum()
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * precision * recall / (precision + recall)
    return (accuracy, precision, recall, f1)


def evaluate_model(
    model,
    on="train",
    plot_cmat=False,
    verbose=True,
    dataset=None,
):
    """
    This function evaluates a model and returns the metrics.
    It can be used to evaluate the model on the training set or the test set.
    It can also plot the confusion matrix.
    Parameters
    ----------
    model : object
        The model to be evaluated.
    on : str, optional
        The set on which the model will be evaluated. The default is "train".
    plot_cmat : bool, optional
        Whether to plot the confusion matrix. The default is False.
    verbose : bool, optional
        Whether to print the metrics. The default is True.

    Returns
    -------
    result : dict
        A dictionary with the metrics.

    Example
    -------
    >>> result = evaluate_model(model)
    >>> print(result)
    {'accuracy': 0.8, 'precision': 0.8, 'recall': 0.8, 'f1': 0.8, 'auc': 0.8}

    >>> result = evaluate_model(model, on="test")
    >>> print(result)
    {'accuracy': 0.8, 'precision': 0.8, 'recall': 0.8, 'f1': 0.8, 'auc': 0.8}

    >>> result = evaluate_model(model, plot_cmat=True)
    >>> print(result)
    {'accuracy': 0.8, 'precision': 0.8, 'recall': 0.8, 'f1': 0.8, 'auc': 0.8}

    >>> result = evaluate_model(model, on="test", plot_cmat=True)
    >>> print(result)
    {'accuracy': 0.8, 'precision': 0.8, 'recall': 0.8, 'f1': 0.8, 'auc': 0.8}
    """
    if on == "train":
        X = dataset[0]
        y = dataset[1]
    else:
        X = dataset[2]
        y = dataset[3]
    y_pred = model.predict(X)
    cm = confusion_matrix(y, y_pred)
    accuracy, precision, recall, f1 = cm_to_metrics(cm)
    auc_score = roc_auc_score(y, y_pred)

    if plot_cmat:
        disp = ConfusionMatrixDisplay(
            confusion_matrix=cm, display_labels=["star", "galaxy"]
        )
        disp.plot()
        plt.show()
    if verbose:
        try:
            model_name = model.__class__.__name__
        except:
            model_name = ""
        print(f"Accuracy on {on} set of the model {model_name}: {accuracy:.4f}")
        print(f"Precision on {on} set of the model {model_name}: {precision:.4f}")
        print(f"Recall on {on} set of the model {model_name}: {recall:.4f}")
        print(f"F1 on {on} set of the model {model_name}: {f1:.4f}")
        print(f"AUC on {on} set of the model {model_name}: {auc_score:.4f}\n")
        cr = classification_report(y, y_pred)
        print(cr)
    result = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "auc": auc_score,
    }
    return result


def dictionary_to_series(dictionary, name):
    """Convert dictionary to pandas series.

    Parameters
    ----------
    dictionary : dict
        Dictionary to convert.
    name : str
        Name of the series.

    Returns
    -------
    series : pandas.Series
        Series with the dictionary values.
    """
    dictionary["model"] = name
    series = pd.Series(dictionary)
    return series


def load_and_update_result(result, filename, name, save=False):
    """
    Load a result from a file and update it with the new result.

    Parameters
    ----------
    result : dict
        The result to be added to the file.
    filename : str
        The name of the file to be updated.
    name : str
        The name of the result.
    save : bool
        Whether to save the file after updating.

    Returns
    -------
    df : pandas.DataFrame
        The updated file.

    Examples
    --------
    >>> load_and_update_result(result, filename, name)
    """

    df = pd.read_csv(filename)
    if name in df["model"].values:
        print(f"Model {name} already exists in the file {filename}.")
        return None
    result_series = dictionary_to_series(result, name)
    result_df = pd.DataFrame(result_series).T
    df = pd.concat([df, result_df], axis=0)
    if save:
        df.to_csv(filename, index=False)
        return None
    return df


def evaluate_and_save_progress(model, name):
    """Evaluate model on train and test set and save the results in a csv file.

    Parameters
    ----------
    model : sklearn model
        Model to evaluate.
    name : str
        Name of the model.

    Returns
    -------
    None.

    Example
    -------
    >>> evaluate_and_save_progress(model, "model_name")
    """
    train_results = evaluate_model(model, on="train", plot_cmat=False, verbose=False)
    test_results = evaluate_model(model, on="test", plot_cmat=False, verbose=False)
    load_and_update_result(
        train_results,
        TRAIN_RESULT_CSV_NAME,
        name,
        save=True,
    )
    load_and_update_result(
        test_results,
        TEST_RESULT_CSV_NAME,
        name,
        save=True,
    )
