from DFT_base import *
from Filters import *

if __name__ == "__main__":
    #Pre-config
    np.set_printoptions(precision=2)

    # Đọc ảnh
    image = cv2.imread("../image/lenna_2.png", cv2.IMREAD_GRAYSCALE)
    # image = cv2.resize(src=image, dsize=(50, 50))

    # Chuyển các pixel của ảnh vào mảng 2 chiều f
    f = np.asarray(image)


    M, N = np.shape(f)  # Chiều x và y của ảnh
    # print(M, N)
    # M, N = 4, 4


    # Bước 1: Chuyển ảnh từ kích thước MxN vào ảnh PxQ với P= 2M và Q =2N
    P, Q = 2 * M, 2 * N
    shape = np.shape(f)


    # Chuyển ảnh PxQ vào mảng fp
    f_xy_p = np.zeros((P, Q))
    f_xy_p[:shape[0], :shape[1]] = f



    # Bước 2: Nhân ảnh fp(x,y) với (-1) mũ (x+y) để tạo ảnh mới
    # Kết quả nhân lưu vào ma trận ảnh fpc
    F_xy_p = np.zeros((P, Q))
    for x in range(P):
        for y in range(Q):
            F_xy_p[x, y] = f_xy_p[x, y] * np.power(-1, x + y)
            # print("F_xy_p[" + str(x) + ", " + str(y) + "] = " + str(F_xy_p[x, y]))

    # print(F_xy_p)


    # Bước 3: Chuyển đổi ảnh Fpc sang miền tần số (DFT)
    dft_cot = dft_hang = np.zeros((P, Q),dtype=complex)
    # DFT theo P - theo cột
    for i in range(P):
        dft_cot[i] = dft_1d(F_xy_p[i])
    # DFT theo Q - theo hàng
    for j in range(Q):
        dft_hang[:, j] = dft_1d(dft_cot[:, j])

    # print("dft_cot: ", dft_cot)
    print("dft_hang: ", dft_hang)
    print("end")


    # Bước 4: Gọi hàm GaussianLP tạo bộ lọc thông thấp Gaussian
    # H_uv = gen_gaussian_high_pass_filter(30, P, Q)
    # H_uv = gen_butterworth_high_pass_filter(60,P,Q,2)
    H_uv = gen_butterworth_low_pass_filter(30,P,Q,2)
    # H_uv = gen_ideal_low_pass_filter(60, P, Q)
    # H_uv = gen_ideal_high_pass_filter(10, P, Q)
    
    # print("H_uv: ", H_uv)

    # Bước 5: Nhân ảnh sau khi DFT với ảnh sau khi lọc
    G_uv = np.multiply(dft_hang, H_uv)
    # print("G[u,v] = " + str(G_uv))

    # Bước 6:
    # Bước 6.1 Thực hiện biến đổi ngược DFT
    idft_cot = idft_hang = np.zeros((P, Q))
    # chuyển đổi DFT ngược theo P - theo cột
    for i in range(P):
        idft_cot[i] = idft_1d(G_uv[i])
    # Chuyển đổi DFT ngược theo Q - theo hàng
    for j in range(Q):
        idft_hang[:, j] = idft_1d(idft_cot[:, j])

    # print("idft_cot: ", idft_cot)
    # print("idft_hang: ", idft_hang)

    # Bước 6.2: Nhân phần thực ảnh sau khi biến đổi ngược với -1 mũ (x+y)
    g_array = np.asarray(idft_hang.real)
    P, Q = np.shape(g_array)
    g_xy_p = np.zeros((P, Q))
    for x in range(P):
        for y in range(Q):
            g_xy_p[x, y] = g_array[x, y] * np.power(-1, x + y)


    # print("Before (g_array): ", g_array)
    # print("After (g_xy_p): ", g_xy_p)

    # Bước 7: Rút trích ảnh kích thước MxN từ ảnh PxQ
    # Và đây ảnh cuối cùng sau khi lọc
    g_xy = g_xy_p[:shape[0], :shape[1]]
    # print("g_xy: ", g_xy)

    # Hiển thị ảnh
    fig = plt.figure(figsize=(16, 9))  # Tạo vùng vẽ tỷ lệ 16:9
    # Tạo 9 vùng vẽ con
    (ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9) = fig.subplots(3, 3)

    # Đọc và hiển thị ảnh gốc

    ax1.imshow(image, cmap='gray')
    ax1.set_title('Ảnh gốc MxN')
    ax1.axis('off')


    # Hiển thị ảnh mở rộng có kích thước PxQ

    ax2.imshow(f_xy_p, cmap='gray')
    ax2.set_title('Bước 1: Ảnh PxQ')
    ax2.axis('off')

    # Hiển thị ảnh sau khi nhân -1 mũ (x+y)
    ax3.imshow(F_xy_p, cmap='gray')
    ax3.set_title('Bước 2: nhân -1 mũ x+y')
    ax3.axis('off')

    # Hiển thị phổ tần số cảu anh sau khi biến đổi Fourier
    # cộng 1e-9 để tránh log(0)
    ax4.imshow(np.abs(dft_hang) + 1e-9, cmap='gray')
    ax4.set_title('Bước 3: Phổ tần số ảnh sau khi DFT')
    ax4.axis('off')

    # Hiển thị phổ tần số của bộ lọc
    ax5.imshow(H_uv, cmap='gray')
    ax5.set_title('Bước 4: Phổ tần số Bộ lọc')
    ax5.axis('off')

    # Hiển thị phổ tần số của kết quả sau khi nhân Phổ tần số sau khi DFT với bộ lọc
    ax6.imshow(np.log(np.abs(G_uv) + 1e-9), cmap='gray')
    ax6.set_title('Bước 5: Sau khi nhân DFT với ảnh sau khi lọc ')
    ax6.axis('off')

    # Hiển thị ảnh sau khi biến đổi ngược
    ax7.imshow(np.log(np.abs(idft_hang) + 1e-9), cmap='gray')
    ax7.set_title('Bước 6.1: Thực hiện DFT ngược')
    ax7.axis('off')

    # Hiển thị phần thực của ảnh sau khi nhân -1 mũ (x+y)
    ax8.imshow(g_xy_p, cmap='gray')
    ax8.set_title('Bước 6.2: Phần thực sau IDFT nhân -1 mũ (x+y)')
    ax8.axis('off')

    # Hiển thị ảnh cuối cùng sau các bước, là ảnh cải thiện kích thước MxN
    ax9.imshow(g_xy, cmap='gray')
    ax9.set_title('Bước 7: Ảnh cuối cùng MxN')
    ax9.axis('off')

    output_path = '../result_image/ideal_highpass_example.png'

    plt.savefig(output_path)
    print(f"Hình ảnh đã được lưu tại: {output_path}")

    plt.show()




