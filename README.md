# Pokémon Cafe and Kirby Cafe Reservation System

Original is from https://github.com/cloudsystemsarchitect/pokemon-cafe-booking
I altered the code to work with Windows and Edge, and to work with the updated website (07.02.2024).

The Pokémon Cafe reservation site now has a captcha. The script now waits for the user to fill out the captcha and then continues the automation process.

I also added uv support and a Python script to run the code without the need for Jupyter notebooks.

## Installation

1. Install [uv](https://docs.astral.sh/uv/getting-started/)
2. Set up the workspace with

```shell
uv sync
```

## Usage

### Pokémon Cafe Reservation Script

The `pokemon-cafe-reservation.py` script automates the booking process for the Pokémon Cafe in Tokyo or Osaka. It uses Selenium to interact with the reservation website.

#### Steps to Use:

1. Ensure you have the necessary dependencies installed, including Selenium and the Edge WebDriver.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with the desired parameters:

```shell
uv run pokemon-cafe-reservation.py --day_of_month <day> --num_of_guests <guests> --location <location> --iterations <iterations>
```

#### Parameters:

- `--day_of_month`: The day of the month to book (e.g., 10).
- `--num_of_guests`: The number of guests to book (1-8).
- `--location`: The location of the cafe ('Tokyo' or 'Osaka').
- `--iterations`: The number of iterations to run the booking (default is 2).

Example:

```shell
uv run pokemon-cafe-reservation.py --day_of_month 10 --num_of_guests 2 --location Tokyo --iterations 2
```

The script will prompt you to solve a CAPTCHA manually before proceeding with the automated booking process.

### Kirby Cafe Reservation Script

The `kirby-cafe-reservation.py` script automates the booking process for the Kirby Cafe in Tokyo. It uses Selenium to interact with the reservation website.

#### Steps to Use:

1. Ensure you have the necessary dependencies installed, including Selenium and the Edge WebDriver.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with the desired parameters:

```shell
python kirby-cafe-reservation.py --num_of_guests <guests> --iterations <iterations>
```

#### Parameters:

- `--num_of_guests`: The number of guests to book.
- `--iterations`: The number of iterations to run the booking (default is 1).

Example:

```shell
python kirby-cafe-reservation.py --num_of_guests 2 --iterations 1
```
