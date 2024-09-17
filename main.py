from datetime import datetime

def parse_time(time_str):
    if len(time_str) == 3:
        time_str = '0' + time_str
    return datetime.strptime(time_str, "%H%M")

def calculate_work_hours(times):
    sorted_times = sorted(times)
    
    total_duration = sorted_times[-1] - sorted_times[0]
    
    lunch_break = sorted_times[2] - sorted_times[1]
    
    work_duration = total_duration - lunch_break
    return work_duration.total_seconds() / 3600 

def get_time_input(prompt):
    while True:
        time_str = input(prompt)
        try:
            return parse_time(time_str)
        except ValueError:
            print("Formato de hora incorreto, por favor insira no padrão HHmm (ex: 730 ou 0730 para 7:30).")

def main():
    print("Por favor insira as suas hora trabalhadas no formato HHmm (ex: , 730 ou 0730 para 7:30 AM)")
    print("Voce pode inserir na ordem que quiser:")
    
    times = []
    labels = ["de entrada", "de sída para almoço", "de término do almoçp", "do fim do expediente"]
    
    for label in labels:
        time = get_time_input(f"Insira o horário {label}: ")
        times.append(time)
    
    total_hours = calculate_work_hours(times)
    
    print(f"\nTotal de horas trabalhadas: {total_hours:.2f}")

if __name__ == "__main__":
    main()