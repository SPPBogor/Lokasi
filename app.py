from flask import Flask, render_template
import csv

app = Flask(__name__)

def load_lokasi_toko():
    toko_list = []
    with open('lokasi.txt', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')  # file kamu pakai TAB
        for row in reader:
            if len(row) < 2:
                continue

            nama = row[0].strip()
            koordinat = row[1].split(',')

            if len(koordinat) != 2:
                continue

            try:
                lat = float(koordinat[0].strip())
                lng = float(koordinat[1].strip())
            except ValueError:
                continue

            toko_list.append({
                "nama": nama,
                "lat": lat,
                "lng": lng
            })

    return toko_list


@app.route("/peta_toko")
def peta_toko():
    toko_list = load_lokasi_toko()
    return render_template(
        "peta_toko.html",
        toko_list=toko_list,
        total_toko=len(toko_list)
    )


if __name__ == "__main__":
    app.run(debug=True)
