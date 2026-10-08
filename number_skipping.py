import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
numbers = np.arange(1,21,2)
fig,ax = plt.subplots(figsize=(8,4))
ax.set_xlim(0,10)
ax.set_ylim(0,5)
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.axis("off")
colors = [
    "#FFFFFF",
    "#F5F5F5",
    "#EEEEEE",
    "#E0E0E0",
    "#D0D0D0",
    "#C0C0C0",
    "#B0B0B0",
    "#A0A0A0",
    "#909090",
    "#808080"
]
number_text = ax.text(
    0,2.5,"Hello",
    fontsize=60,
    ha="center",
    va="center",
    fontweight="bold"
)
def update(frame):
  number = numbers[frame]
  x_position = frame*0.5
  number_text.set_position((x_position,2.5))
  number_text.set_text(number)
  number_text.set_color(colors[frame%len(colors)])
  return number_text,
animation = FuncAnimation(fig,update,frames=len(numbers),
                          interval=100,repeat=True)
plt.close(fig)
from IPython.display import HTML, display
display(HTML(animation.to_jshtml()))
