# Speech Animation Framework

A modular, browser-based framework for speech production and perception experiments using animated visual stimuli. Built with **jsPsych**, compatible with **JATOS** and **Prolific**, and designed for reusable, language-independent experimental workflows.

## Overview

The Speech Animation Framework is an open-source toolkit for designing and running browser-based speech production and perception experiments. It combines reusable animated visual stimuli, integrated browser-based audio recording, flexible perception paradigms, and standardized data collection into a single modular framework.

Originally developed for research on the interface between prosody, syntax, and information structure, the framework is language-independent and can readily be adapted to a wide range of experimental paradigms in linguistics, speech science, psycholinguistics, and related fields.

The repository includes complete example production and perception experiments in **English**, **German**, and **Hungarian**, together with supporting documentation and utilities for downstream analysis.

---

## Features

- Browser-based experiments requiring no software installation for participants
- Speech production experiments with integrated browser-based audio recording
- Speech perception paradigms including rating, forced-choice, and ranking tasks
- Reusable animated visual stimuli for controlled speech elicitation
- Modular architecture built with **jsPsych**
- Language-independent design suitable for cross-linguistic research
- Automatic collection of responses, reaction times, metadata, and audio recordings
- Compatible with **JATOS**, **MindProbe**, and **Prolific**
- Output suitable for analysis in **R**, **Python**, and other statistical software
- Python utility for extracting recorded audio from experimental output
- Open-source and fully customizable under the MIT License

---

## Screenshots

### Animated Visual Stimulus

Example animation used to elicit controlled speech production.

*(insert screenshot here)*

### Speech Production Interface

Example production experiment with integrated browser-based audio recording.

*(insert screenshot here)*

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/akos-buza/speech-animation-experimental-framework.git
cd speech-animation-experimental-framework
```

### 2. Start a local web server

```bash
python -m http.server 8000
```

### 3. Open an experiment

Navigate to

```
http://localhost:8000
```

and open one of the example experiment files, for example:

- `production-index-english.html`
- `production-index-german.html`
- `production-index-hungarian.html`
- `perception-english.html`
- `perception-german.html`
- `perception-hungarian.html`

Allow microphone access when prompted.

---

## Repository Structure

```
speech-animation-experimental-framework/
│
├── production-index-english.html
├── production-index-german.html
├── production-index-hungarian.html
│
├── perception-english.html
├── perception-german.html
├── perception-hungarian.html
│
├── audioplaceholder.wav
├── audio-extract-animation-task.py
│
├── ANIMATION_TASK_DOCUMENTATION_GITHUB_VERSION.pdf
├── README.md
├── CITATION.cff
└── LICENSE
```

The production and perception experiments share the same underlying architecture and can be adapted to new languages or experimental paradigms by modifying the participant instructions and linguistic materials while preserving the experimental logic and animations.

---

## Documentation

Complete documentation is available in

```
ANIMATION_TASK_DOCUMENTATION_GITHUB_VERSION.pdf
```

The documentation describes:

- production and perception workflows
- animation design
- customization
- deployment with JATOS
- data output
- example information-structural conditions
- repository organization

---

## Citation

If you use this framework in your research, please cite the repository using the provided `CITATION.cff` file.

---

## License

This project is released under the MIT License.
