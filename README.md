# CV Assignment

Solutions to the 25 questions, split across three sub-tasks.

## Structure

```text
1_Basic_Image_Handling/              Q1-Q10  — read/save, grayscale, display, resize
2_Pixel_Image_Representation/        Q11-Q20 — pixel access, channels, stats, synthetic images
3_Sampling_Quantization_Geometric/   Q21-Q25 — bit quantization, downsampling, crop, rotate
```

Each folder is self-contained:

- a script covering that sub-task's questions
- `assignment_1_cv.jpg` — local copy of the input image
- `output/` — where results get written

## Running

```bash
git clone https://github.com/Unreal-coder-1807/CV_uni_assignment.git
cd CV_uni_assignment
pip install -r requirements.txt
python 1_Basic_Image_Handling/1_basic_image_handling.py
python 2_Pixel_Image_Representation/2_pixel_image_representation.py
python 3_Sampling_Quantization_Geometric/3_sampling_quantization_geometric.py
```

Scripts run headlessly — no display windows, results (and relevant stats printed to console) go straight into each `output/` folder. Paths are resolved relative to the script itself, so they work from any working directory.
