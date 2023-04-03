# Data to Include

Columns which we are going to use:
`PhotoPrimary` View

- objID, run, camcol, field (For identification)
- rowv, colv (all deg/day)
- modelFlux\_{c}, {c}, psfMag\_{c} (mag or nanomaggies)
- petroRad\_{c}, deVRad\_{c}, expRad\_{c} (arcsec)
- q\_{c}, u\_{c}, expAB\_{c} (Some ratios)
- ra, dec, b, l (for position)
- type

> {c} = u, g, r, i, z

Conditions which we are going to use:

- nChild = 0
- clean = 1

```sql
  (sa.specObjID=0) and
  (sa.psfmag_u < 35) and
  (sa.psfmag_g < 35) and
  (sa.psfmag_r < 35) and
  (sa.psfmag_i < 35) and
  (sa.psfmag_z < 35) and
  (sa.psfmag_u > 0) and
  (sa.psfmag_g > 0) and
  (sa.psfmag_r > 0) and
  (sa.psfmag_i > 0) and
  (sa.psfmag_z > 0) and
```

The query is

```sql
SELECT objID, run, camcol, field, type, -- identification
rowv, colv, -- velocity
u, g, r, i, z, -- modelMag
psfMag_u, psfMag_g, psfMag_r, psfMag_i, psfMag_z, -- psfMag
modelFlux_u, modelFlux_g, modelFlux_r, modelFlux_i, modelFlux_z, -- modelFlux
petroRad_u, petroRad_g, petroRad_r, petroRad_i, petroRad_z, -- petroRad
expRad_u, expRad_g, expRad_r, expRad_i, expRad_z, -- expRad
q_u, q_g, q_r, q_i, q_z, -- q ratio
u_u, u_g, u_r, u_i, u_z, -- u ratio
expAB_u, expAB_g, expAB_r, expAB_i, expAB_z, -- exp a/b ratio
ra, dec, b, l -- position
INTO MyDB.data_1
FROM PhotoPrimary
WHERE
  (nchild = 0) and
  (clean = 1) and
  (type = 3) and -- galaxy
  (specObjID=0) and
  (psfmag_u < 35) and
  (psfmag_g < 35) and
  (psfmag_r < 35) and
  (psfmag_i < 35) and
  (psfmag_z < 35) and
  (psfmag_u > 0) and
  (psfmag_g > 0) and
  (psfmag_r > 0) and
  (psfmag_i > 0) and
  (psfmag_z > 0)

--order by OBJID
ORDER BY objID

--paging
OFFSET 0 ROWS
FETCH NEXT 100000 ROWS ONLY
```

The offset and the next rows will be changed. Also, `type = 3` (which correspond to galaxy) will be changed to `type = 6` for stars.
