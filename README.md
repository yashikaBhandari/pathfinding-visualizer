# Graph Pathfinding Visualizer

An **interactive pathfinding visualizer** built using **Python** and **Pygame** that demonstrates popular shortest path algorithms: **Dijkstra**, **Breadth-First Search (BFS)**, and **Depth-First Search (DFS)**.

## 🚀 Features

* Interactive grid UI built with Pygame
* Implements 3 shortest path algorithms:

  * Dijkstra's Algorithm
  * Breadth-First Search (BFS)
  * Depth-First Search (DFS)
* Visual feedback for each algorithm
* Barrier creation, node placement, reset functionality

---

## 🛠 Tools & Technologies

* **Python 3.9+**
* **Pygame** library

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yashikaBhandari/pathfinding-visualizer.git
cd pathfinding-visualizer
```

### 2. Set Up Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # for Mac/Linux
venv\Scripts\activate     # for Windows
```

### 3. Install Dependencies

```bash
pip install pygame
```

---

## ▶️ How to Run

```bash
python3 main.py
```

### 🖱️ Mouse Actions

| Action              | Effect                       |
| ------------------- | ---------------------------- |
| 🟩 Left-click once  | Place **start node** (green) |
| 🟥 Left-click again | Place **end node** (red)     |
| ⬛ Left-click more   | Draw **barriers** (black)    |
| 🧹 Right-click      | Erase any cell               |

### ⌨️ Keyboard Controls

| Key | Action                       |
| --- | ---------------------------- |
| B   | Run **Breadth First Search** |
| D   | Run **Depth First Search**   |
| K   | Run **Dijkstra's Algorithm** |
| R   | **Reset** the grid           |

---


+-------------------------------------------------+
|                                                 |
|   S = Start Node (Green)                         |
|   E = End Node (Red)                             |
|   ■ = Wall (Black)                              |
|   ○ = Empty Walkable Node (White)               |
|   ▓ = Visited Nodes during search (Blue/Yellow)|
|   ★ = Final Path (Purple)                        |
|                                                 |
|  How to interact:                                |
|  1. Left-click once to place Start (S)          |
|  2. Left-click again to place End (E)            |
|  3. Left-click & drag to draw Walls (■)          |
|  4. Press Spacebar (or assigned key) to start    |
|     algorithm visualization                      |
|                                                 |
|  Example grid:                                   |
|                                                 |
|  ○ ○ ○ ○ ○ ○ ○ ○ ○ ○                             |
|  ○ S ○ ■ ■ ○ ○ ○ E ○                             |
|  ○ ○ ○ ■ ○ ○ ○ ■ ■ ○                             |
|  ○ ○ ○ ■ ○ ○ ○ ○ ○ ○                             |
|                                                 |
+-------------------------------------------------+

## 🧠 Algorithms Explained

* **BFS**: Explores all neighbors at the current depth before going deeper.
* **DFS**: Explores as far as possible down one path before backtracking.
* **Dijkstra**: Uses a priority queue to always pick the node with the smallest cost.

---

## 🧩 File Structure

```
graph-pathfinding-visualizer/
├── main.py             # Main app controller
├── grid.py             # Grid creation, drawing, interaction
├── algorithms.py       # Algorithm implementations
└── README.md           # Project description
```

---

## 🎯 Future Improvements

* Add **A* algorithm*\*
* Add **maze generation**
* Deploy to web using **PyScript** or **JS translation**

---

## 📸 Screenshots
![Uploading Screenshot 2025-05-24 at 5.34.08 PM.png…]()




![Uploading Screenshot 2025-05-24 at 5.34.27 PM.png…]()


---

## 🧑‍💻 Author

**Yashika Bhandari**
[GitHub](https://github.com/yashikaBhandari)
[LinkedIn](https://www.linkedin.com/in/yashika-bhandari-ab7a74253/)

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
