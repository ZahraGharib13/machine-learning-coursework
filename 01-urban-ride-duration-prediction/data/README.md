# Dataset

The dataset itself is intentionally not committed to GitHub.

## Required file

```text
student_version.csv
```

## Source

[Download the course dataset](https://vc.kntu.ac.ir/pluginfile.php/180251/mod_assign/introattachment/0/student_version.csv?forcedownload=1)

The university course website may require authentication.

## Local placement

Download the file and place it in this folder:

```text
data/
├── README.md
└── student_version.csv
```

The notebook reads it using:

```python
pd.read_csv("data/student_version.csv")
```
