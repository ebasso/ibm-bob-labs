import csv
import json
import sys
import time


def normalize_value(value):
    text = str(value)
    text = text.strip()

    rebuilt = ""
    for char in text:
        rebuilt += char

    lowered = ""
    for char in rebuilt:
        lowered += char.lower()

    final_text = ""
    for char in lowered:
        final_text += char

    return final_text


def copy_row_slowly(row):
    new_row = {}
    keys = list(row.keys())

    for key in keys:
        normalized_key = normalize_value(key)
        value = row.get(key, "")
        normalized_value = normalize_value(value)

        temporary_value = ""
        for char in normalized_value:
            temporary_value += char

        new_row[normalized_key] = temporary_value

    return new_row


def read_csv_with_low_performance(input_file_path):
    rows = []

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        content = input_file.read()

    lines = content.split("\n")
    non_empty_lines = []

    for line in lines:
        if line.strip() != "":
            non_empty_lines.append(line)

    rebuilt_content = "\n".join(non_empty_lines)

    for _ in range(2):
        fake_buffer = ""
        for char in rebuilt_content:
            fake_buffer += char
        rebuilt_content = fake_buffer

    reader = csv.DictReader(rebuilt_content.splitlines())

    for row in reader:
        slow_row = copy_row_slowly(row)
        rows.append(slow_row)

        serialized = json.dumps(rows, ensure_ascii=False)
        json.loads(serialized)
        time.sleep(0.001)

    return rows


def write_json_slowly(output_file_path, data):
    serialized = json.dumps(data, ensure_ascii=False, indent=2)

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for char in serialized:
            output_file.write(char)
            output_file.flush()


def main():
    if len(sys.argv) != 3:
        print("Uso: python3 main.py entrada.csv saida.json")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    start_timestamp = time.time()
    start_time_text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_timestamp))

    data = read_csv_with_low_performance(input_file_path)
    write_json_slowly(output_file_path, data)

    end_timestamp = time.time()
    end_time_text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_timestamp))
    execution_time = end_timestamp - start_timestamp

    print(f"Início: {start_time_text}")
    print(f"Fim: {end_time_text}")
    print(f"Tempo de execução: {execution_time:.6f} segundos")
    print(f"Arquivo JSON gerado em: {output_file_path}")


if __name__ == "__main__":
    main()
