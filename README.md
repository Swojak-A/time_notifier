# time_notifier
Simple program and its Windows distribution that annouce every full hour.

## How to use distribution?

1. Clone repository.

2. (Optional) Copy contents of `dist/` folder into the choosen directory. 

3. Execute `time_notifier.exe` to run program in the background.

## How to create distribution using provided code?

### Setup

Setup info:
- Python: 3.4.4
- pipenv: 2018.11.26

**Warning! Any version of Python above 3.6 will fail to create distribution due to py2exe limitations.**

### How to create distribution? Easy step-by-step guide

1. Download `pipenv` and `Python 3.4.4`.

2. Clone the repository

3. (Optional) Delete `dist` directory - just in case.

4. (Optional) Run `export PIPENV_VENV_IN_PROJECT=1` to locate virtual enviroment directory in the project directory.

5. In the repositorys directory run `pipenv install` to install virtual enviroment.

6. (Optional) Modify if needed.

7. Run ` python setup.py install`

8. Run `python setup.py py2exe` It will create distribution, which should now be in `dist` directory.
