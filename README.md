# Speech Animation Framework

A modular, browser-based framework for speech production and perception experiments using animated visual stimuli. Built with jsPsych, compatible with JATOS and Prolific, and designed for reusable, language-independent experimental workflows.



## Overview

The **Speech Animation Framework** is an open-source toolkit for designing and running browser-based speech production and perception experiments. It combines reusable animated visual stimuli, integrated browser-based audio recording, flexible perception paradigms, and standardized data collection into a single modular framework.

Although originally developed for research on the interface of **prosody, syntax, and information structure**, the framework is language-independent and can readily be adapted to a wide range of experimental paradigms in linguistics, speech science, psycholinguistics, and related fields.

The framework supports the complete experimental workflow—from stimulus presentation and speech recording to online perception experiments and reproducible data analysis—while remaining compatible with platforms such as **jsPsych**, **JATOS**, **Prolific**, and statistical environments including **R** and **Python**.


## Features

- **Browser-based experiments** — no software installation required for participants.
- **Speech production tasks** with integrated browser-based audio recording.
- **Speech perception paradigms**, including rating, forced-choice, ranking, and custom response interfaces.
- **Reusable animated visual stimuli** for eliciting controlled speech production.
- **Modular architecture** built with jsPsych for easy customization and extension.
- **Language-independent design**, allowing adaptation to a wide range of linguistic experiments.
- **Automatic data collection**, including responses, reaction times, metadata, and audio recordings.
- **Compatible with JATOS and MindProbe** for online deployment and data management.
- **Suitable for Prolific** and other online participant recruitment platforms.
- **Standardized output formats** for downstream analysis in **R** and **Python**.
- **Open-source and fully customizable** for research and teaching purposes.
## Screenshots

### Animated Visual Stimulus

Example of a reusable animated stimulus used to elicit controlled speech production.

<p align="center">
  <img width="875" alt="Animated visual stimulus" src="https://github.com/user-attachments/assets/3cdad20b-a9cc-4e52-9151-1d69be62dc37">
</p>

### Speech Production Interface

Example of a production experiment combining animated stimuli with integrated browser-based audio recording.

<p align="center">
  <img width="682" alt="Speech recording interface" src="https://github.com/user-attachments/assets/79238c58-cbb3-4fdf-8fd0-abc76924cc54">
</p>


## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/<username>/speech-animation-framework.git
cd speech-animation-framework
```

### 2. Launch a local server

```bash
python -m http.server 8000
```

Then open your browser and navigate to:

```
http://localhost:8000
```

### 3. Run an example experiment

Open one of the example production or perception experiments in your browser, or deploy the framework through JATOS for online data collection.

For detailed installation, customization, and deployment instructions, see the **User Guide** in the `docs/` directory.

## Repository Structure

```
speech-animation-framework/
│
├── animations/      Reusable animation components
├── production/      Speech production experiments
├── perception/      Speech perception experiments
├── stimuli/         Example stimulus materials
├── analysis/        R and Python analysis scripts
├── docs/            User Guide and additional documentation
└── media/           Audio and visual assets
```

The framework is organized into independent modules that can be adapted or extended without modifying the overall architecture.
