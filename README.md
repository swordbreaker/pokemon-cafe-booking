# Pokémon Cafe Reservation System

Original is from https://github.com/cloudsystemsarchitect/pokemon-cafe-booking
I altered the code to work with Windows and Edge, and to work with the updated website (07.02.2024).

The Pokémon Cafe reservation site now has a captcha. The script now waits for the user to fill out the captcha and then continues the automation process.

I also added uv support and a Python script to run the code without the need for Jupyter notebooks:

1. Install [uv](https://docs.astral.sh/uv/getting-started/)
2. Set up the workspace with

```shell
uv sync
```

3. Alter the variables at the bottom of the script
4. Run the scripts with

```shell
uv run pokemon-cafe-reservation.py
# or
uv run kirby-cafe-reservation.py
```

---
This notebook is a simple script for automating the booking process at the Pokémon Cafe in Tokyo, Japan. It is written in a Jupyter notebook, so just open the pokemon-cafe-reservation.ipynb and follow the steps. This notebook uses the Python library Selenium to automate the reservation process.

Have Fun!
