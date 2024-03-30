from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
	print("\nCHUONG TRINH QUAN LY SINH VIEN")
	print("**********************MENU**************************")
	print("** 1. Thêm sinh viên                              **")
	print("** 2. Cập nhật thông tin sinh viên bởi ID         **")
	print("** 3. Xóa sinh viên bởi ID                        **")
	print("** 4. Tìm kiếm sinh viên theo tên                 **")
	print("** 5. Sắp xếp sinh viên theo tên chuyên ngành     **")
	print("** 6. Sắp xếp sinh viên theo tên chuyển ngành     **")
	print("** 7. Hiển thị danh sách sinh viên.               **")
	print("** 0. Thoát                                       **")
	print("****************************************************")

	key = int(input("Nhap tuy chon:"))
	if(key == 1):
		print("\n. Thêm sinh viên.")
		qlsv.nhapSinhVien()
		print("\n Thêm sinh viên thành công!")
	elif(key == 2):
		if(qlsv.soLuongSinhVien()>0):
			print("\n2. Cập nhật thông tin sinh viên.")
			print("\n Nhập ID:")
			ID = int(input())
			qlsv.updateSinhVien(ID)
		else:
			print("\n Danh sách sinh viên trong!")
	elif (key==3):
			if(qlsv.soLuongSinhVien()>0):
				print("\n 3. Xóa sinh viên.")
				print("\nNhập ID:")
				ID = int(input())
				if (qlsv.deleteById(ID)):
					print("\nSinh Viên có id =", ID,"đã bị xóa")
				else:
					print("\n Sinh viên có ID=",ID,"không tồn tại.")
			else:
				print("\n Danh sách sinh viên trong!")
	elif(key == 4):
			if(qlsv.soLuongSinhVien()>0):
				print("\n5. Sắp xếp sinh viên theo điểm trung bình(GPA).")
				qlsv.sortByDiemTB()
				qlsv.showSinhVien(qlsv.getListSinhVien())
			else:
				print("\n Danh sách sinh viên trong!")
	elif (key == 6):
			if(qlsv.soLuongSinhVien()>0):
				print("\n6. Sắp xếp sinh viên theo tên.")
				qlsv.sortByName()
				qlsv.showSinhVien(qlsv.getListSinhVien())
			else:
				print("\nDanh sách sinh vien trong!")
	elif(key == 7):
			if(qlsv.soLuongSinhVien()>0):
				print("\n7. Hiển thị danh sách sinh viên. ")
				qlsv.showSinhVien(qlsv.getListSinhVien())
			else:
				print("\nDanh sách sinh viên trong!")
	elif(key == 0):
			print("\n Bạn đã chọn thoát chương trình!")
			break
	else:
			print("\n không có chức năng này!")
			print("\n Hãy chọn chức năng trong hợp menu.")