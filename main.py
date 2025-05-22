import logging
import time
from fetch_data import fetch_ohlcv
from indicators import add_indicators
from signal_generator import generate_signal
from telegram_bot import send_telegram_message

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main_loop():
    while True:
        try:
            logging.info("Fetching market data...")
            df = fetch_ohlcv(symbol="ETH/USDT", timeframe="5m")

            logging.info("Calculating indicators...")
            df = add_indicators(df)

            logging.info("Generating signal...")
            signal = generate_signal(df)

            message = f"ETH 5m Signal: *{signal}*"
            logging.info(f"Sending message: {message}")
            send_telegram_message(message)

        except Exception as e:
            logging.error(f"Unexpected error: {e}")

        logging.info("Sleeping for 5 minutes...\n")
        time.sleep(300)  # Sleep for 5 minutes (300 seconds)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    df = fetch_ohlcv()
    print(df.tail())
    main_loop()
