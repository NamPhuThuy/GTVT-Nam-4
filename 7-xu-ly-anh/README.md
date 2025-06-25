<a id="readme-top"></a>

- [Chương 1: Tổng quan về xử lý ảnh](#chương-1-tổng-quan-về-xử-lý-ảnh-image-processing)
  - [Phần 1: Các thành phần của digital image](#phần-1-các-thành-phần-của-digital-image)
  - [Phần 2: Một số mô hình màu](#phần-2-một-số-mô-hình-màu)
  - [Phần 3: Phần 3: Xử lý ảnh là gì? Ứng dụng của xử lý ảnh](#phần-3-xử-lý-ảnh-là-gì-ứng-dụng-của-xử-lý-ảnh)
  - [Phần 4: Các giai đoạn của quá trình xử lý ảnh](#phần-4-các-giai-đoạn-của-quá-trình-xử-lý-ảnh)
- [Chương 2: Thu nhận ảnh và biểu diễn ảnh](#chương-2-thu-nhận-ảnh-và-biểu-diễn-ảnh)
  - [Phần 1: Thu nhận ảnh](#phần-1-thu-nhận-ảnh-image-acquisition)
  - [Phần 2: Biểu diễn ảnh](#phần-2-biểu-diễn-ảnh-digital-image-representation)
- [Chương 3: Cải thiện hình ảnh](#chương-3-cải-thiện-hình-ảnh)
  - [Phần 1: Cải thiện hình ảnh là gì?](#phần-1-cải-thiện-hình-ảnh-là-gì)
  - [Phần 2: Miền không gian](#phần-2-miền-không-gian)
  - [Phần 3: Miền tần số](#phần-3-miền-tần-số)
  - [Phần 4: Combination](#phần-4-combination)

# Chương 1: Tổng quan về xử lý ảnh (Image Processing)
## Phần 1: Các thành phần của digital image
Ảnh kỹ thuật số (**digital image**) có thể được biểu diễn dưới dạng 1 ma trận 2 chiều f(x, y). Trong đó, x, y là tọa độ của mỗi điểm ảnh (pixel), và f là cường độ (**intensity**) hoặc mức xám (**gray level**) tại điểm ảnh đó  
<img src="images/img-01-01.png" width = "400px">

Điểm ảnh (**pixel**) là 1 phần tử của ảnh kỹ thuật số với tọa độ và mức xám nhất định  
<img src="images/img-01-02.png" width = "400px">
<p align="right">(<a href="#readme-top">back to top</a>)</p>

Mức xám (**gray scale**) là thang đo độ sáng của 1 điểm ảnh trong đoạn **[0, 255]**
<table>
    <tr>
        <th>Ảnh</th>
        <th>Ma trận của ảnh</th>
    </tr>
    <tr>
        <td><img src="images/img-01-03.png" alt="Image description" width="300px"></td>
        <td><img src="images/img-01-04.png" alt="Image description" width="300px"></td>
    </tr>
</table>

Độ sâu màu (**color depth**), còn gọi là **bit depth**, chỉ số lượng bit được dùng để thể hiện màu của 1 pixel trên ảnh  
<img src="images/img-01-05.png" width="400">

Độ phân giải của ảnh (**image resolution**), là số lượng pixel được sử dụng để thể hiện ảnh  
<img src="images/img-01-06.png" width="400">

Phân loại digital image
- Binary image: ảnh nhị phân, chỉ có 2 màu đen-trắng  
<img src="images/img-01-07.png" width="400">

- Gray image: ảnh xám, được xây dựng từ 1 ma trận màu  
<img src="images/img-01-08.png" width="400">

- Color image: ảnh màu, được xây dựng từ nhiều ma trận màu  
<img src="images/img-01-09.png" width="400">

## Phần 2: Một số mô hình màu
### Mô hình màu cộng (Additive color model)
#### RGB - Red-Green-Blue
<img src="images/img-01-10.png" width="400">

#### HSV - Hue-Saturation-Value
<img src="images/img-01-11.png" width="400">

### Mô hình màu trừ (Subtractive color model)
#### CMYK-Cyan-Magenta-Yellow-Black
<img src="images/img-01-12.png" width="400">

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Phần 3: Xử lý ảnh là gì? Ứng dụng của xử lý ảnh
Xử lý ảnh (**image processing**) là 1 lĩnh vực Khoa học máy tính (**computer science**). liên quan đến việc thao tác với ảnh kỹ thuật số (**digital image**) để trích xuất thông tin hoặc nâng cao chất lượng của chúng

Một số ứng dụng của **Xử lý ảnh**:  
- Y tế:
  - Phân tích X-quang: Phát hiện các bất thường như khối u hoặc gãy xương.
  - Chụp CT: Tạo mô hình 3D của các cơ quan nội tạng để chẩn đoán và lập kế hoạch phẫu thuật.
  - Chụp MRI: Hình ảnh hóa các mô mềm và phát hiện các bệnh như ung thư.

- Xe tự lái:
  - Phát hiện vật thể: Nhận dạng người đi bộ, phương tiện và biển báo giao thông.
  - Phát hiện làn đường: Phát hiện vạch kẻ làn đường để lái xe tự động.
  - Phát hiện chướng ngại vật: Tránh va chạm với chướng ngại vật.

- An ninh và giám sát:
  - Nhận dạng khuôn mặt: Nhận dạng cá nhân cho mục đích an ninh. 
  - Theo dõi vật thể: Theo dõi chuyển động của các vật thể trong một cảnh. 
  - Nhận dạng biển số xe: Tự động nhận dạng biển số xe.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Phần 4: Các giai đoạn của quá trình xử lý ảnh
<img src="images/img-01-13.png" width="400">
<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Chương 2: Thu nhận ảnh và biểu diễn ảnh
## Phần 1: Thu nhận ảnh (Image Acquisition)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Phần 2: Biểu diễn ảnh (Digital image representation)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Chương 3: Cải thiện hình ảnh
## Phần 1: Cải thiện hình ảnh là gì?
Cải thiện hình ảnh (**image enhancement**) là quá trình xử lý kỹ thuật số để cải thiện chất lượng của hình ảnh thông quá các khía cạnh của ảnh như: độ tương phản (**contrast**), độ sáng (**brightness**), độ sắc nét (**sharpness**), giảm nhiễu (**noise reduction**)

<img src="images/img-03-01.png" width="400">
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Phần 2: Miền không gian
(**spatial domain**)
Hầu hết các phép toán cải thiện ở miền không gian (**spatial domain enhancement operations**) có thể được rút gọn thành dạng: 

$$
**g (x, y) = T[ f (x, y)]**
$$
- $f(x, y)$: ảnh đầu vào
- $g(x, y)$: ảnh đã xử lý
- $T$: toán tử được áp dụng vào vùng lân cận của (x, y)

<img src="images/img-03-02.png" width="400">

### Kỹ thuật xử lý điểm
Khi vùng lân cận đạt mức nhỏ nhất (size = 1*1) - bằng đúng 1 điểm ảnh, các phép toán cải thiện ảnh sẽ được biểu diễn thành: 

$$
s = T(r)
$$
- $r$: điểm ảnh trước khi xử lý
- $s$: điểm ảnh sau khi được xử lý

<img src="images/img-03-03.png" alt="Image description" width="400px">

<table>
    <tr>
        <td><img src="images/img-03-04.png" alt="Image description" width="400px"></td>
    </tr>
    <tr>
      <th>Một số biến đổi mức xám</th>
    </tr>
</table>

#### Ảnh âm bản (**negative image**)
<table>
    <tr>
        <td><img src="images/img-03-05.png" alt="Image description" width="400px"></td>
    </tr>
    <tr>
        <th>mammogram and negative image of mammogram</th>
    </tr>
</table>

Ảnh âm bản dùng để làm nổi bật các chi tiết  
$s = intensity_{max} — r$

#### Biến đổi Logarit (Logarithm transformation)
Công thức chung của biến đổi logarit: $s = c * log(1 + r)$. Giá trị $c$ thường được đặt là 1

Kỹ thuật dùng để tăng cường độ sáng các vùng tối của ảnh 

<img src="images/img-03-06.png" alt="Image description" width="400px">

#### Biến đổi luật lũy thừa (Power Law - Gamma Correction Transformations)
Công thức chung: $s = c*r^{\gamma}$. Giá trị $c$ thường là 1

<img src="images/img-03-07.png" alt="Image description" width="400px">

<table>
    <tr>
        <td><img src="images/img-03-08.png" alt="Image description" width="350px"></td>
        <td><img src="images/img-03-09.png" alt="Image description" width="350px"></td>
    </tr>
    <tr>
        <th>Highlight</th>
        <th>Làm tối ảnh</th>
    </tr>
</table>

#### Biến đổi ngưỡng (Threasholding)

<table>
    <tr>
        <td><img src="images/img-03-10.png" alt="Image description" width="400px"></td>
    </tr>
</table>

Biến đổi ngưỡng hữu ích cho việc phân đoạn (**segmentation**), khi chúng ta muốn tách những vật thể ra khỏi background
- Đặt ngưỡng thấp -> hình ảnh thu được sẽ chứa nhiều giá trị cường độ cao. Và ngược lại

### Các kỹ thuật biến đổi tuyến tính từng phần
Ta có thể áp dụng những phép biến đổi khác nhau cho mỗi ngưỡng, để thu được ảnh kết quả theo ý muốn  

<table>
    <tr>
        <td><img src="images/img-03-11.png" alt="Image description" width="400px"></td>
    </tr>
    <tr>
        <td><img src="images/img-03-12.png" alt="Image description" width="400px"></td>
    </tr>
</table>

#### Cắt mặt phẳng bit (bit plane slicing)
Bằng cách tách biệt các bit cụ thể của giá trị pixel trong hình ảnh, chúng ta có thể làm nổi bật các khía cạnh nhất định của hình ảnh đó.

<table>
    <tr>
        <td><img src="images/img-03-13.png" alt="Image description" width="400px"></td>
    </tr>
    <tr>
        <td><img src="images/img-03-14.png" alt="Image description" width="400px"></td>
    </tr>
</table>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Phần 3: Miền tần số
(**frequency domain**)

### Histogram 

Biểu đồ histogram của hình ảnh cho chúng ta biết sự phân bố các mức độ xám trong hình ảnh. Hữu ích trong xử lý hình ảnh, đặc biệt là trong phân đoạn (**segmentation**) và cải thiện ảnh (**enhancement**).

<table>
    <tr>
        <td><img src="images/img-03-15.png" alt="Image description" width="400px"></td>
    </tr>
    <tr>
        <th>Hình ảnh và biểu đồ histogram của chúng</th>
    </tr>
</table>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Chương 4: Lọc trong miền tần số

## Phần 1: Định nghĩa
- Biến đổi Fourier (Fourier Transform) dùng để chuyển ảnh từ miền không gian (spatial domain) sang miền tần số (frequency domain)
- Decompose into sine and cosine components
- Ứng dụng trong: phân tích ảnh (image analysis), lọc ảnh (image filtering), tái tạo ảnh (image reconstruction), nén ảnh (image compression)

<img src="images/Fourier_transform_application.png" alt="Image 2 description" width=400px>

<img src="images/Image_Filtering_Process.png" alt="Image 2 description" width=400px>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Phần 2: Ứng dụng
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Phần 3: Biến đổi Fourier

<img src="images/Fast_fourier_transform.png" alt="Image 2 description" width=400px>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Phần 4: DCT
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Phần 5: DWT
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Phần 6: SVD
<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Chương 5: Khôi phục ảnh 
Khôi phục ảnh (**image restoration**)

## Phần 1: Mô hình khôi phục/thoái hóa ảnh
Mô hình suy thoái (**degradation model**) là quá trình thêm nhiễu vào 1 ảnh gốc **f(x, y)** ban đầu để tạo ra Image Degradation (ảnh suy thoái - có chất lượng thấp hơn ảnh ban đầu) - **g(x, y)**

Mô hình khôi phục (**restoration model**) là quá trình khôi phục ảnh khi biết trước h(x, y) và \delta
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<img src="images/c5_1.png" alt="Image 2 description" width=400px>  
<img src="images/c5_2.png" alt="Image 2 description" width=400px>  
<img src="images/c5_3.png" alt="Image 2 description" width=400px>  

## Phần 2: Hiệu suất
<img src="images/c5_2_MSE.png" alt="Image 2 description" width=400px>  

- MSE: Mean-Squared Errors - Dùng để tính trung bình của **tổng bình phương sai số** giữa 2 ảnh
- f(x, y): ảnh gốc
- f^(x, y): ảnh sau khôi phục

<img src="images/c5_3_SNR.png" alt="Image 2 description" width=400px>

- SNR: Signal Noise Ratio

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)" title="" />

h<sub>&theta;</sub>(x) = &theta;<sub>o</sub> x + &theta;<sub>1</sub>x


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Phần 3: Mô hình nhiễu
Một mô hình nhiễu (**noise model**) mô tả những đặc tính cả 1 loại nhiễu trong ảnh, mỗi loại noise model sẽ có 1 bộ lọc nhiễu (noise filter) tương ứng để xử lý

Nguyên nhân của nhiễu ảnh thường gây ra bởi quá trình thu nhận ảnh (image acquisition) hoặc quá trình truyền ảnh (image transimission)
- Ví dụ:
  - Các yếu tố như ánh sáng, nhiệt độ có thể ảnh hưởng tới chất lượng ảnh khi chụp ảnh
  - Truyền ảnh không dây (wireless)


Một số mô hình nhiễu (Noise model)
- Salt and Pepper
- Gausian
- Speckle
- Impulse

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Phần 4: Restoration for Noise-Only Degradation – Spatial Filtering, Mean Filters, Order-Statistic Filters

### Mean Filters
#### 3. Harmonic Mean Filter
It works well for salt noise, Gaussian noise. But fails for pepper noise


#### 4. Contra-Harmonic Mean Filter
Used for:
- Salt and pepper noise.
  - Q > 0: eliminate pepper noise
  - Q < 0: eliminate salt noise

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Phần 5: Restoration for Blur-Only Degradation-Wiener Filtering
<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Chương 6: Xử lý ảnh hình thái
Image processing morphological

## Phần 1

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

## Hit or Miss Transform

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Chương 7

Phân vùng (Segmentation) là quá trình chia ảnh thành các vùng có mối quan hệ gần nhau
![](images/image_segmentation.png)  
Phân vùng ảnh dựa vào 2 đặc trung cơ bản của intensity values:
- Discontinuity (tính rời rạc, gián đoạn): Partitioning the image into regions based on sudden changes in intensity, such as edges
- Similarity (tính tương tự):

## Discontinuity detection
Có 3 loại gray level discontinuities:
- Edges
- Lines

## Phần 1: 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Tài liệu tham khảo
- [What is Digital Image Processing? | Image Processing #1](https://medium.com/@gokcenazakyol/1-what-is-digital-image-processing-image-processing-2da13b5dfa9c) - Medium
- [What is Image Enhancement? | Image Processing #3](https://medium.com/@gokcenazakyol/what-is-image-enhancement-image-processing-3-32a813087e0a) - Medium