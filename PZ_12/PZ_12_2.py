# ��������� ��������� (yield), ������� ����������� ��� ��������� ������� � ��������.
def letters(low: str):
    for n in low:
        yield n.lower()


a = input("������� �������: ")
print("".join(letters(a)))