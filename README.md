# CV Assignment — Day 1

Solutions to the 25 Python + OpenCV coding questions from `Computer_Vision_Day_1_25_Coding_Questions.pdf`, split across three sub-tasks.

## Structure

```
1_Basic_Image_Handling/              Q1-Q10  — read/save, grayscale, display, resize
2_Pixel_Image_Representation/        Q11-Q20 — pixel access, channels, stats, synthetic images
3_Sampling_Quantization_Geometric/   Q21-Q25 — bit quantization, downsampling, crop, rotate
```

Each folder is self-contained:
- a script covering that sub-task's questions
- `assignment_1_cv.jpg` — local copy of the input image
- `output/` — where results get written

## Running

```
python 1_Basic_Image_Handling/1_basic_image_handling.py
python 2_Pixel_Image_Representation/2_pixel_image_representation.py
python 3_Sampling_Quantization_Geometric/3_sampling_quantization_geometric.py
```

Scripts run headlessly — no display windows, results (and relevant stats printed to console) go straight into each `output/` folder. Paths are resolved relative to the script itself, so they work from any working directory.

Requires: `opencv-python`, `numpy`, `matplotlib`.
