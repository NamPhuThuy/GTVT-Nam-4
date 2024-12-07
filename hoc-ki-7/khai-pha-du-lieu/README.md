# Chương trình học 
Nội dung của học phần này sẽ tìm hiểu bám sát theo cuốn **Data Mining - Concepts and Techniques**
Giảng viên: Nguyễn Quốc Tuấn
Tính điểm: 0.4 * Điểm quá trình + 0.6 * Điểm thi KTHP

## Tổng quan nội dung học
- Tìm hiểu về từng bước của quá trình Khai phá dữ liệu: thu nhận data -> làm sạch data ->... -> lưu trữ data
- Có thể sử dụng các công cụ có sẵn (Rapid Miner,..) hoặc tự code (Python, R,..)
- Bài tập lớn: 
  - Xây dựng 1 ứng dụng khai phá dữ liệu với bài toán cụ thể
  - Tối đa 5 người
  - Không yêu cầu ứng dụng có giao diện
- Chương 1: Giới thiệu về Khai phá dữ liệu
- Chương 2, 3: Các bước tiền xử lý dữ liệu
- Chương 6, 7: Bài toán khai phá nội kết hợp
- Chương 8, 9: Bài toán phân loại dữ liệu
- Chương 10, 11: Bài toán phân cụm dữ liệu

# Đề cương K62
## Format bài thi
- Thi tự luận, thời gian 75'
- Câu  1 (6đ): 
  - Kiến thức chương 2, 3
  - Gồm 5 ý (Cho 1 bảng dữ liệu)
    - Ý 1: Tính độ lệch chuẩn, trung bình, trung vị
    - Ý 2: Vẽ biểu đồ box-plot
    - Ý 3: Làm trơn dữ liệu (mean, median, boundaries). Có 2 dạng bài: chia bin theo chiều rộng và chiều sâu 
    - Ý 4: Chuẩn hóa data, theo min-max/z-score
    - Ý 5: Tính hệ số tương quan 
- Câu 2 (4đ): 1 trong 3 dạng dưới đây
  - Dạng 1: Khai phá nội kết hợp
    - Ý 1: Cho sup count, tìm tập phổ biến
    - Ý 2: Cho độ tin cậy tối thiểu -> xác định các luật kết hợp mạnh

  - Dạng 2: Bài toán phân lớp (hỏi về cây quyết định, không thi Naive Bayes) 
    - Ý 1 (3đ): Từ tập dữ liệu, xây dựng cây quyết định bằng thuật toán ID3/C4.5
    - Ý 2 (1đ): Cho 1 dataset mẫu, áp dụng vào cây quyết định ở ý 1 để tìm kết quả
    
  - Dạng 3: Bài toán phân cụm (vào K-mean, không thi K-medoids)
    - Cho số K, vị trí của K tâm ban đầu
    - Ý 1 (2đ): Hỏi, sau vòng lặp đầu: 
      - Tâm của mỗi cụm nằm ở đâu?
      - Mỗi cụm sẽ gồm những điềm nào?
    - Ý 2 (2đ): Kết quả cuối cùng thi được sẽ gồm những cụm nào?

## Đề ôn tập mẫu
Câu 1. Cho tập dữ liệu thu thập được của 2 tập giá trị của X và Y như sau:

- Hãy xác định các giá trị trung bình, trung vị, mode của X và Y. 
- Vẽ biểu đồ Boxplot của X và Y. 
- Sử dụng phương pháp chuẩn hóa min-max để chuẩn hóa dữ liệu quan sát của X và Y về đoạn [1, 5]. 
- Hãy làm trơn dữ liệu ban đầu của X và Y bằng phương pháp làm trơn trung bình (bin means), trong đó việc phân chia thùng theo chiều sâu (Equal-depth) với số bin là 3. Mô tả các bước thực hiện. 
- Xác định hệ số tương quan giữa X và Y.
