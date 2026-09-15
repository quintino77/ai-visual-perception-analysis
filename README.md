# Human Perception of AI-Generated Faces

A focused portfolio review of published research on visual authenticity judgments, age and viewing devices. Includes a reproducible English graphic and LinkedIn draft.

## Question
Does age relate to people's ability to distinguish real photographs from AI-generated portraits, and can research support a simple decline from 2022 to 2026?

## Evidence
- Nightingale & Farid (2022): the first experiment reported 48.2% classification accuracy for real and StyleGAN2 faces, near 50% chance. This contradicts the claim that all AI faces were easy to identify in 2022. https://doi.org/10.1073/pnas.2120481119
- Kim & Kim (2026 preprint): 1,664 adults aged 20–69; mobile n=1,330 and PC n=334. Published age slopes were -0.607 percentage points/year on mobile and -0.230 on PC. https://arxiv.org/abs/2603.24048

## Method
The graphic rescales published slopes by ten: -0.607 × 10 = -6.07 and -0.230 × 10 = -2.30 percentage points per ten-year age difference. Bars display the magnitude of the associated decrease. These are between-person associations, not longitudinal aging effects, age-group averages, or percent changes. No participant-level data were collected or reanalyzed for this project.

## Interpretation and limitations
Age was negatively associated with performance in this study, particularly on mobile. Device cohorts were observational, so device causation is not established. Older PC participants were sparsely sampled. Overall accuracy was 85.24%, so the study does not support a universal inability to distinguish real from synthetic faces. Images were generated in July 2025; testing ran August 2025–January 2026. Publication in 2026 does not make this a benchmark of September 2026 models. The preprint findings are provisional.

The studies use different images, participants and methods; their accuracy figures must not be joined into a time-series trend. Neither establishes conclusions about video, all older adults, teenagers, or the Brazilian population. Showing causal progress in generator realism would require a matched evaluation across model vintages, content and age groups.

## Reproduce
Python 3 with matplotlib:

```sh
python -m pip install -r requirements.txt
python create_chart.py
```

## Files
- `create_chart.py`: chart source and documented values.
- `AI_Visual_Perception.png`: image for LinkedIn.
- `linkedin_post.md`: English post draft.
- `requirements.txt`: plotting dependency.

## Portfolio use
Present this as a literature-based analysis project. It demonstrates evidence appraisal, quantitative interpretation, visualization and communication; it is not an original participant study or proof of employment experience.

