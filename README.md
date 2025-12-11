Variant Annotation Pipeline

This is a simple variant annotation project for genetics research.

#Project Structure

variant-annotation-pipeline/
 ├── sample.vcf          # Input VCF file
 ├── annotate.py         # Python script
 ├── annotated_output.csv # Output CSV (generated)
 ├── README.md           # Project info
 └── requirements.txt    # Python dependencies

#How to Run

1. Install Python (>=3.8 recommended)
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the script:

```
python annotate.py
```

4. Check `annotated_output.csv` for output.
