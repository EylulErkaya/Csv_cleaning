import pandas as pd

input_csv_path = "vindr_detection_v1_folds.csv"
output_csv_path = "vindr_detection_v1_folds_tekrarsiz.csv"

# Ayni olanlari kontrol etmek istediğin sütunlari buraya yaz
kontrol_sutunlari = ['image_id']

df = pd.read_csv(input_csv_path, sep= ";")
#print("Sütunlar:", df.columns.tolist())


# Belirtilen sütunlara göre ayni olanlardan sadece ilkini birak, diğerlerini sil
df_tekrarsiz = df.drop_duplicates(subset=kontrol_sutunlari, keep='first')

df_tekrarsiz.to_csv(output_csv_path, index=False)

print("Tekrarlayan satirlar silindi ve yeni CSV kaydedildi.")
