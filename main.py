import pandas as pd
import sys
import argparse
from data_extractor import create_new_excel_data
from statistics_calculator import calculate_statistics, prepare_final_data
from excel_writer import write_to_excel
from sort import custom_sort
from update_fa_column import update_fa_column

parser = argparse.ArgumentParser()
parser.add_argument("input_file_path", help="Path to the input Excel file")
parser.add_argument("base_file_path", help="Path to the base Excel file")
parser.add_argument("--tlocation", action="store_true", help="Create tlocation with FA")
parser.add_argument("--statistics", action="store_true", help="Create statistics sheet")
parser.add_argument("--both", action="store_true", help="Run both processes sequentially")

args = parser.parse_args()

input_file_path = args.input_file_path
base_file_path = args.base_file_path

output_file_path = 'tlocation.xlsx'

if args.both:
    data = create_new_excel_data(input_file_path)

    df = pd.DataFrame(data, columns=["Cabinet", "Location", "Type", "Channel", "KKS", "CIR", "CONNECTION"])

    # Добавляем новый столбец FA
    df["FA"] = ""

    sorted_df = df.sort_values(by=["Cabinet", "Location"], key=lambda col: col.map(custom_sort))

    with pd.ExcelWriter(output_file_path, mode='w') as writer:
        sorted_df.to_excel(writer, sheet_name='tlocation', index=False)

    # Обновление столбца FA
    update_fa_column(output_file_path, base_file_path)

    module_types = ['DI', 'AI', 'DO', 'AO', 'AI-R']
    module_stats, channel_stats, cabinet_stats = calculate_statistics(df, module_types)

    final_data = prepare_final_data(module_stats, channel_stats, cabinet_stats)

    write_to_excel(final_data, output_file_path)

elif args.tlocation:
    data = create_new_excel_data(input_file_path)

    df = pd.DataFrame(data, columns=["Cabinet", "Location", "Type", "Channel", "KKS", "CIR", "CONNECTION"])

    # Добавляем новый столбец FA
    df["FA"] = ""

    sorted_df = df.sort_values(by=["Cabinet", "Location"], key=lambda col: col.map(custom_sort))

    with pd.ExcelWriter(output_file_path, mode='w') as writer:
        sorted_df.to_excel(writer, sheet_name='tlocation', index=False)

    # Обновление столбца FA
    update_fa_column(output_file_path, base_file_path)

elif args.statistics:
    data = pd.read_excel(input_file_path)

    module_types = ['DI', 'AI', 'DO', 'AO', 'AI-R']
    module_stats, channel_stats, cabinet_stats = calculate_statistics(data, module_types)

    final_data = prepare_final_data(module_stats, channel_stats, cabinet_stats)

    write_to_excel(final_data, output_file_path)

print(f"Process completed. Output saved to {output_file_path}")
