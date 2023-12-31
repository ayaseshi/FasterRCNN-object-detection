import matplotlib.pyplot as plt

def plot_losses(losses, val_losses):
    epochs = range(1, len(losses) + 1)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(epochs, losses, label='Training Loss', marker='o', linestyle='-')
    ax.plot(epochs, val_losses, label='Validation Loss', marker='o', linestyle='-')

    ax.set_xlabel('Epochs')
    ax.set_ylabel('Loss')
    ax.set_title('Training and Validation Loss Over Time')

    ax.legend()
    ax.grid(True)

    fig.set_facecolor('#f0f0f0')

    return fig

def plot_accuracies(train_accuracies, test_accuracies, val_accuracies):
    epochs = range(1, len(train_accuracies) + 1)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(epochs, train_accuracies, label='Training Accuracy', marker='o', linestyle='-')
    ax.plot(epochs, test_accuracies, label='Test Accuracy', marker='o', linestyle='-')
    ax.plot(epochs, val_accuracies, label='Validation Accuracy', marker='o', linestyle='-')

    ax.set_xlabel('Epochs')
    ax.set_ylabel('Accuracy')
    ax.set_title('Test, Validation, and Training Accuracy Over Time')

    ax.legend()
    ax.grid(True)

    fig.set_facecolor('#f0f0f0')

    return fig