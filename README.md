# Synthetic-Data-for-Scam-Detection-Leveraging-LLMs-to-Train-Deep-Learning-Models

This repository contains the source code and synthetic datasets used in our research on scam detection using deep learning models trained on data generated by Large Language Models (LLMs). Our work demonstrates the effectiveness of synthetic data in training scam detection models and offers publicly available datasets and models for further research and development in fraud prevention.

## Overview

This research presents a novel approach to training scam detection models using synthetic data generated by Large Language Models (LLMs). We propose single-agent and multi-agent methods for data generation and train six deep learning architectures—LSTM, BiLSTM, GRU, BiGRU, CNN, and BERT—to classify conversations as scam or non-scam. Our experiments demonstrate that models trained on synthetic data achieve high accuracy on both generated test sets and real-world scam conversations. The models perform well even with limited conversation turns and when analyzing only the suspect's messages, indicating potential for early scam detection and privacy-preserving applications. Our findings highlight the efficacy of synthetic data in overcoming real-world dataset limitations for scam detection. 

### Key Contributions:
1. Synthetic datasets were generated using single-agent and multi-agent conversation.
2. Models were trained to classify conversations as scam or non-scam, achieving high accuracy on synthetic and real-world data.
3. Models were evaluated for early scam detection and privacy-preserving methods by analyzing suspect-only messages.

## Datasets

Two datasets were generated using LLMs:
1. **Single-Agent Dataset**: A single LLM was used to simulate both the scammer’s and victim’s conversations. This dataset includes 1,600 conversations split evenly between scam and non-scam categories.
2. **Multi-Agent Dataset**: Two LLM instances were configured, one representing the scammer/non-scammer and the other acting as the victim with various personality traits (e.g., skeptical, trusting, aggressive). This dataset also includes 1,600 conversations.

**Scam Categories:**
- Social Security Scams
- Refund Scams
- Technical Support Scams
- Reward Scams

**Non-Scam Categories:**
- Delivery Confirmations
- Insurance Sales
- Appointment Confirmations
- Wrong number

The dataset and models for this project are available on [[Hugging Face](https://huggingface.co/)]. You can download them directly using the links below:
- **Dataset**: 
  - [Single Agent Scam Conversations](https://huggingface.co/datasets/BothBosu/single-agent-scam-conversations)
  - [Multi Agent Scam Conversations](https://huggingface.co/datasets/BothBosu/multi-agent-scam-conversation)
  - [YouTube Scam Conversations](https://huggingface.co/datasets/BothBosu/youtube-scam-conversations)
- **Trained Model**: 
  - [Trained Scam Detection Model](https://huggingface.co/collections/BothBosu/synthetic-data-for-scam-detection-66bd8c555bdd611f9af82511)
  
### Results

Below are the plots illustrating the performance of various models:

**Single-Agent Dataset:**
![Model Accuracy vs  Number of Turns (Single-Agent Dataset)](https://github.com/user-attachments/assets/99d98454-8328-4023-86f9-381294912715)

**Multi-Agent Dataset:**
![Model Accuracy vs  Number of Turns (Multi-Agent Conversation Dataset)](https://github.com/user-attachments/assets/0295faf1-8b07-4beb-8d66-209b71f71ae5)

**Single-Agent Dataset with only Suspect:**
![Model Accuracy vs  Number of Turns with only Suspect (Single-Agent Datset)](https://github.com/user-attachments/assets/51009cd9-9e10-421e-b663-dd2aa8c38f87)

**Multi-Agent Dataset with only Suspect:**
![Model Accuracy vs  Number of Turns with only Suspect (Multi-Agent Conversation Datset)](https://github.com/user-attachments/assets/782ec49c-52b1-4d7e-8fad-e9330792c00a)

**YouTube Video Dataset (Trained on Single-Agent Dataset):**
![Model Accuracy vs  Number of Turns on Youtube Videoes (Trained on Single-Agent Dataset)](https://github.com/user-attachments/assets/de4258ea-8bb7-4e54-9f96-833b6611e3d8)

**YouTube Video Dataset (Trained on Multi-Agent Dataset):**
![Model Accuracy vs  Number of Turns on Youtube Videos (Trained on Multi-Agent Dataset)](https://github.com/user-attachments/assets/81490b2a-71ab-42f6-a65f-929d0fa14c87)

**YouTube Video Dataset with only Suspect (Trained on Single-Agent Dataset):**
![Model Accuracy vs  Number of Turns with only Suspect on Youtube Videos (Trained on Single-Agent Datset)](https://github.com/user-attachments/assets/37da378d-0344-42d6-92c8-844db6ff60e2)

**YouTube Video Dataset with only Suspect (Trained on Multi-Agent Dataset):**
![Model Accuracy vs  Number of Turns with only Suspect on Youtube Videos (Trained on Multi-Agent Datset)](https://github.com/user-attachments/assets/65b27aa1-81da-41cd-907c-21fe3f07ece8)

### Conclusion 
This research demonstrates that deep learning models trained entirely on synthetic data can effectively detect scam conversations, even from limited information such as only the suspect's messages. This privacy-preserving approach is highly applicable in real-world scenarios, allowing telecom companies and messaging platforms to detect potential fraud without processing full conversations. Future research should focus on expanding the diversity of synthetic datasets and further improving model architectures to support real-time scam detection systems.

### Clone the repository:
```bash
git clone https://github.com/yourusername/scam-detection-using-synthetic-data.git
cd Synthetic-Data-for-Scam-Detection-Leveraging-LLMs-to-Train-Deep-Learning-Models
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

## Citing This Work

If you use this repo, please cite:

```
@inproceedings{gumphusiri2024,
  title={Synthetic Data for Scam Detection: Leveraging LLMs to Train Deep Learning Models},
  author={Gumphusiri, Pitipat and Triyason, Tuul},
  year={2024},
  booktitle={IEEE/WIC International Conference on Web Intelligence and Intelligent Agent Technology (under review)},
}
```
