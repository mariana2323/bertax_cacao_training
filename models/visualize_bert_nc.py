import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Ana Acosta/Documents/Tesis/pre-training_results/def_1_878208/bert_nc_loss_history.csv")

plt.plot(df["epoch"], df["loss"], label="Training Loss")
plt.plot(df["epoch"], df["val_loss"], label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()