## Morphological
- Morphological operations (Các phép toán hình thái) là 1 tập hợp các kỹ thuật được dùng trong **Xử lý ảnh** để phân tích và chỉnh sửa hình dạng và cấu trúc của các đối tượng trong 1 ảnh

Một số phép toán hình thái
- Erosion (Xói mòn): Thu hẹp ranh giới của các đối tượng trong một hình ảnh. 
- Dilation (Giãn nở): Mở rộng ranh giới của các đối tượng trong một hình ảnh. 
- Opening (Mở): Xóa các đối tượng nhỏ và nhiễu khỏi một hình ảnh. 
- Closing (Đóng): Lấp đầy các lỗ hổng bên trong các đối tượng và xóa các khoảng trống nhỏ giữa các đối tượng. 
- Hit-or-miss: Phát hiện các mẫu hoặc hình dạng cụ thể trong một hình ảnh. 
- Skeletonization: Giảm một đối tượng thành bộ xương hoặc trục giữa của nó.

## Set Theory
![](images/set_theory.png)

## Logic operators 
![](images/logic_operators.png)

## Reflection of Structural Element
Phần tử cấu trúc (Structural Element - SE):
- Là 1 ma trận được sử dụng trong các phép toán hình thái
- Ví dụ

  | 0 | 1 | 0 |
  |---|---|---|
  | 1 | 1 | 1 |
  | 0 | 1 | 0 |

Phép phản chiếu (reflection) là phép quay 180 độ của **phần tử cấu trúc** xung quanh điểm trung tâm 

### Hit, Fit, Miss
- Fit: occurs when **all** the pixels of the SE match the pixels of the image
- Hit: occurs when **any** pixel of the SE match a pixel of the image
- Miss: occurs when **no** pixel of the SE match any pixel of the image
- Ví dụ  
Với 2 Structural Element như sau
<table>
  <tr>
    <td><img src="images/SE_1.png" alt="Image 1 description " width=200px> <br> <p align="center">SE 1</p>
    </td>
    <td><img src="images/SE_2.png" alt="Image 2 description" width=200px><br> <p align="center">SE 2</p></td>
  </tr>
</table>

<table>
  <td><img src="images/matrix.png" alt="Image 1 description " width=400px > <br> <p align="center">Ma trận mẫu</p>
  </td>
</table>

SE_1 áp dụng lên:
- Khu vực A: Hit  
- Khu vực B: Fit  
- Khu vực C: Miss  

SE_2 áp dụng lên:
- Khu vực A: Fit (chỉ cần tất cả số '1' của SE nằm trùng với các số '1' của sub_box, các số '0' của SE thì không cần quan tâm)
- Khu vực B: Fit
- Khu vực C: Miss

## Một số phép toán hình thái
### Erosion
SE sử dụng:

| 0 | 1 | 0 |
|---|---|---|
| 1 | 1 | 1 |
| 0 | 1 | 0 |

Ma trận ban đầu:  

| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Cách làm**

<img src="images/erosion_formula.png" alt="Image 2 description" width=200px><br>
- Giải thích
  - A: cửa sổ đang xét trên ma trận ban đầu
  - B: SE (Structural Element)
  - A^c: phần bù của A


- Sử dụng SE như 1 cái cửa sổ, xét lần lượt từng ma trận con trong ma trận ban đầu (các ma trận con này có cùng cỡ với SE)
- Nếu xảy ra **hiện tượng Fit** thì giá trị tại vị trí đấy ở ma trận mới sẽ bằng 1, còn lại thì bằng 0


Ma trận sau khi xử lý:

| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |


<table>
  <tr>
    <td><img src="images/erosion_input_example.png" alt="Image 1 description " width=200px> <br> <p align="center">Input</p>
    </td>
    <td><img src="images/erosion_output_example.png" alt="Image 2 description" width=200px><br> <p align="center">Output</p></td>
  </tr>
</table>

### Dilation
SE sử dụng:

| 0 | 1 | 0 |
|---|---|---|
| 1 | 1 | 1 |
| 0 | 1 | 0 |

Ma trận ban đầu:

| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Cách làm**

<img src="images/dilation_formula.png" alt="Image 2 description" width=200px><br>

- Sử dụng SE như 1 cái cửa sổ, xét lần lượt từng ma trận con trong ma trận ban đầu (các ma trận con này có cùng cỡ với SE)
- Nếu xảy ra **hiện tượng Hit** thì giá trị tại vị trí đấy ở ma trận mới sẽ bằng 1, còn lại thì bằng 0

Ma trận sau khi xử lý:

| 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |


<table>
  <tr>
    <td><img src="images/dilation_input_example.png" alt="Image 1 description " width=200px> <br> <p align="center">Input</p>
    </td>
    <td><img src="images/dilation_output_example.png" alt="Image 2 description" width=200px><br> <p align="center">Output</p></td>
  </tr>
</table>

### Closing and Opening
- Opening: thực hiện phép co (Erosion) rồi giãn (Dilation)

<img src="images/opening_fomula.png" alt="Image 2 description" width=200px><br>
<img src="images/opening_example.png" alt="Image 2 description" width=500px><br>

- Closing: thực hiện phép giãn (Dilation) rồi co (Erosion)  

<img src="images/closing_formula.png" alt="Image 2 description" width=200px><br>