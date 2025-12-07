while True: #Lập đến khi nào ng dùng 
    while True:
        distance_input = input("Nhập quãng đường đã đi (km): ")
        try:
            distance = float(distance_input)
            if distance >= 0:
                break
            else:
                print("Khoảng cách không được nhỏ hơn 0, nhập lại.")
        except: 
            print("Bạn phải nhập số, nhập lại.")

    print("Bạn đã đi được:", distance, "km")

    while True:
        kind = input("Bạn có đi xe điện không (y/n)?: ").lower().strip()
        if kind in ("y", "n"):
            break
        else:
            print("Chỉ được chọn y hoặc n")

    if kind == "y": #Đi xe điện
        while True:
            try:
                energy = float(input("Mức tiêu hao (kWh/100km): "))
                if energy >= 0:
                    break
                else:
                    print("Không được nhỏ hơn 0, nhập lại.")
            except:
                print("Bạn phải nhập số, nhập lại.")

        while True:
            try:
                price = float(input("Giá điện (đồng/kWh): "))
                if price >= 0:
                    break
                else:
                    print("Không được nhỏ hơn 0, nhập lại.")
            except:
                print("Bạn phải nhập số, nhập lại.")

        total_energy = energy * distance / 100
        total_cost = total_energy * price

        print("Tổng điện tiêu thụ:", total_energy, "kWh")
        print("Tổng chi phí:", total_cost, "đồng")

    else: #Đi xe thường ko phải xe điện
        while True:
            try:
                fuel = float(input("Mức tiêu hao (lít/100km): "))
                if fuel >= 0:
                    break
                else:
                    print("Không được nhỏ hơn 0, nhập lại.")
            except:
                print("Bạn phải nhập số, nhập lại.")

        while True:
            try:
                price = float(input("Giá xăng (đồng/lít): "))
                if price >= 0:
                    break
                else:
                    print("Không được nhỏ hơn 0, nhập lại.")
            except:
                print("Bạn phải nhập số, nhập lại.")

        total_fuel = fuel * distance / 100
        total_cost = total_fuel * price

        print("Tổng nhiên liệu tiêu thụ:", total_fuel, "lít")
        print("Tổng chi phí:", total_cost, "đồng")

    while True:
        again = input("Bạn có muốn tính toán lại không (y/n)?: ").lower().strip()
        if again in ("y", "n"):
            break
        else:
            print("Chỉ được chọn y hoặc n")
        
    if again != "y":
        print("Xin cảm ơn")
        break
    