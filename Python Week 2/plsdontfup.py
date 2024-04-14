# Me trying to import my tables I wrote

def aaaa(file_path):
    try:
        with open(file_path, 'r') as file:
            table = [list(map(int, row.split())) for row in file.readlines()]
            
        return table
    
    except Exception as e:

        return f"An error occurred: {e}"
