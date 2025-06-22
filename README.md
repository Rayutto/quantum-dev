# quantum-dev

**quantum-dev** is a collaborative environment for developing quantum simulations and visualizations using [QuTiP](http://qutip.org/) inside containers (e.g., via VS Code Dev Containers or Docker).  
It also includes a collection of exercises, examples, and experiments based on the textbook *Introduction à la théorie quantique* (see Acknowledgments).

---

## 📖 Acknowledgments

We thank the authors of the book *Introduction à la théorie quantique* (Éditions Ellipses):

- Michèle Desouter  
- Yves Justum  
- Xavier Chapuisat  

We also acknowledge Michel Menou for his contributions to the exercises.  
Some exercises are reproduced and solved here.  
We **highly recommend** this book to French-speaking readers who want a rigorous and accessible introduction to quantum physics.

---

## 🚀 Getting Started

### 🔧 Requirements

- [Docker](https://www.docker.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### 📦 Using the Dev Container (Recommended)

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/quantum-dev.git
   cd quantum-dev

2.	Open it in VS Code and click:
> Reopen in Container
(or use Command Palette: Ctrl+Shift+P → Dev Containers: Reopen in Container)

This will:
    - Build the container from Dockerfile
    - Install Python, QuTiP, Jupyter, and other dependencies
    - Mount your local code inside the container

You’re ready to code and run simulations!

### 📁 Folder Structure
quantum-dev/
│
├── notebooks/          # Jupyter notebooks (Wigner, Fock, Schrödinger)
├── src/                # Source files for common simulation tools
├── exercises/          # Corrected problems from the textbook
├── devcontainer.json   # VS Code container configuration
├── Dockerfile          # Environment definition
└── requirements.txt    # Python package list


### 🧠 Topics Covered
- Schrödinger equation simulations
- Wigner functions
- Coherent and cat states
- Harmonic oscillator and infinite well
- Operator algebra with QuTiP

⸻

### 🤝 Contributing

We welcome contributions! To contribute:
- Fork the repo
- Create a new branch
- Make your changes
- Submit a pull request

If you’re translating, correcting exercises, or adding new physics notebooks — let us know!

⸻

### 📄 License

This project is released under the MIT License.
Exercise content remains the intellectual property of the original textbook authors. Please use respectfully and with proper citation.

### 💬 Questions?

Feel free to open an issue or discussion on GitHub.