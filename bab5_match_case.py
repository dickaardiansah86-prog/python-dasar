hari = "sabtu"

match hari:
    case "sabtu" | "minggu":
        print("hari libur")
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("hari kerja")