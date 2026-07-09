import csv
import json
import sys
import time


def normalize_value(value):
    return str(value).strip().lower()


def read_csv(input_file_path):
    with open(input_file_path, "r", encoding="utf-8", newline="") as input_file:
        reader = csv.DictReader(input_file)
        return [
            {normalize_value(key): normalize_value(value) for key, value in row.items()}
            for row in reader
        ]


def write_json(output_file_path, data):
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=2)


def main():
    if len(sys.argv) != 3:
        print("Uso: python3 main-high.py entrada.csv saida.json")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    start_timestamp = time.time()
    start_time_text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_timestamp))

    data = read_csv(input_file_path)
    write_json(output_file_path, data)

    end_timestamp = time.time()
    end_time_text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_timestamp))
    execution_time = end_timestamp - start_timestamp

    print(f"Início: {start_time_text}")
    print(f"Fim: {end_time_text}")
    print(f"Tempo de execução: {execution_time:.6f} segundos")
    print(f"Arquivo JSON gerado em: {output_file_path}")


if __name__ == "__main__":
    main()
