import matplotlib.pyplot as plt

from DFT_base import *

# Định nghĩa hàm lọc thông cao GaussianHP
def GaussianHP(D0,U,V):
    # H cho filter
    H = np.zeros((U, V))
    D = np.zeros((U, V))
    U0 = int(U / 2)
    V0 = int(V / 2)
    # Tính khoảng cách
    for u in range(U):
        for v in range(V):
            u2 = np.power(u, 2)
            v2 = np.power(v, 2)
            D[u, v] = np.sqrt(u2 + v2)
    # Tính bộ lọc
    for u in range(U):
        for v in range(V):
            H[u, v] = 1- np.exp((-D[np.abs(u - U0), np.abs(v - V0)] ** 2) / (2 * (D0 ** 2)))

    return H


if __name__ == "__main__":
    #Pre-config
    np.set_printoptions(precision=2)
    
    # Đọc ảnh
    image = cv2.imread("image/4x4pixels.png", 0)
    # image = cv2.resize(src=image, dsize=(50, 50))

    # Chuyển các pixel của ảnh vào mảng 2 chiều f
    f = np.asarray(image)
    # print(f)
    '''
    [[153 153 153 153]
     [102 102 102 102]
     [ 51  51  51  51]
     [  0   0   0   0]]
    '''
    
    M, N = np.shape(f)  # Chiều x và y của ảnh
    # print(M, N)
    # M, N = 4, 4
    
    
    # Bước 1: Chuyển ảnh từ kích thước MxN vào ảnh PxQ với P= 2M và Q =2N
    P, Q = 2 * M, 2 * N
    shape = np.shape(f)
    
    # print(P, Q)
    # print(shape)
    '''
   P, Q = 8, 8
   shape = (4, 4)
   '''
    
    
    # Chuyển ảnh PxQ vào mảng fp
    f_xy_p = np.zeros((P, Q))
    f_xy_p[:shape[0], :shape[1]] = f
    
    # print(f_xy_p)
    '''
    f_xy_p:  
    [[153. 153. 153. 153.   0.   0.   0.   0.]
     [102. 102. 102. 102.   0.   0.   0.   0.]
     [ 51.  51.  51.  51.   0.   0.   0.   0.]
     [  0.   0.   0.   0.   0.   0.   0.   0.]
     [  0.   0.   0.   0.   0.   0.   0.   0.]
     [  0.   0.   0.   0.   0.   0.   0.   0.]
     [  0.   0.   0.   0.   0.   0.   0.   0.]
     [  0.   0.   0.   0.   0.   0.   0.   0.]]
    '''
    

    # Bước 2: Nhân ảnh fp(x,y) với (-1) mũ (x+y) để tạo ảnh mới
    # Kết quả nhân lưu vào ma trận ảnh fpc
    F_xy_p = np.zeros((P, Q))
    for x in range(P):
        for y in range(Q):
            F_xy_p[x, y] = f_xy_p[x, y] * np.power(-1, x + y)
            # print("F_xy_p[" + str(x) + ", " + str(y) + "] = " + str(F_xy_p[x, y]))
            
    # print(F_xy_p)
    '''
    F_xy_p: 
    [[ 153. -153.  153. -153.    0.   -0.    0.   -0.]
     [-102.  102. -102.  102.   -0.    0.   -0.    0.]
     [  51.  -51.   51.  -51.    0.   -0.    0.   -0.]
     [  -0.    0.   -0.    0.   -0.    0.   -0.    0.]
     [   0.   -0.    0.   -0.    0.   -0.    0.   -0.]
     [  -0.    0.   -0.    0.   -0.    0.   -0.    0.]
     [   0.   -0.    0.   -0.    0.   -0.    0.   -0.]
     [  -0.    0.   -0.    0.   -0.    0.   -0.    0.]]
    '''
    

    # Bước 3: Chuyển đổi ảnh Fpc sang miền tần số (DFT)
    dft_cot = dft_hang = np.zeros((P, Q),dtype=complex)
    # DFT theo P - theo cột
    for i in range(P):
        dft_cot[i] = DFT1D(F_xy_p[i])
    # DFT theo Q - theo hàng
    for j in range(Q):
        dft_hang[:, j] = DFT1D(dft_cot[:, j])

    # print(dft_cot)
    # print(dft_hang)
    
    '''
    dft_cot:
    [[ 0.00e+00+0.00e+00j  1.02e+02+4.22e+01j  1.87e-14-2.13e-14j 1.02e+02+2.46e+02j  4.08e+02+7.49e-14j  1.02e+02-2.46e+02j -3.49e-14-3.55e-14j  1.02e+02-4.22e+01j]
    [ 0.00e+00+0.00e+00j  7.21e+01+5.46e+01j  1.78e-14-1.45e-14j 2.99e+01+2.16e+02j  3.24e+02+8.45e+01j  1.32e+02-1.74e+02j -1.74e-14-3.54e-14j  8.96e+01-1.24e+01j]
    [ 0.00e+00+0.00e+00j  5.98e+01+1.44e+02j  3.29e-14-2.58e-15j -1.44e+02+3.48e+02j  4.08e+02+4.08e+02j  3.48e+02-1.44e+02j 7.74e-15-7.75e-14j  1.44e+02+5.98e+01j]
     [ 0.00e+00+0.00e+00j  1.74e+02+2.16e+02j  5.85e-14-1.59e-14j -7.21e+01+6.67e+02j  9.00e+02+4.92e+02j  5.22e+02-4.20e+02j -3.41e-14-1.38e-13j  2.76e+02+2.99e+01j]
     [ 0.00e+00+0.00e+00j  3.06e+02+1.27e+02j  5.62e-14-4.97e-14j 3.06e+02+7.39e+02j  1.22e+03+3.25e-13j  3.06e+02-7.39e+02j -1.19e-13-1.21e-13j  3.06e+02-1.27e+02j]
     [ 0.00e+00+0.00e+00j  2.76e+02-2.99e+01j  2.42e-14-6.11e-14j 5.22e+02+4.20e+02j  9.00e+02-4.92e+02j -7.21e+01-6.67e+02j -1.37e-13-3.63e-14j  1.74e+02-2.16e+02j]
     [ 0.00e+00+0.00e+00j  1.44e+02-5.98e+01j  4.53e-15-4.01e-14j 3.48e+02+1.44e+02j  4.08e+02-4.08e+02j -1.44e+02-3.48e+02j -7.75e-14+6.47e-15j  5.98e+01-1.44e+02j]
     [ 0.00e+00+0.00e+00j  8.96e+01+1.24e+01j  1.19e-14-2.23e-14j 1.32e+02+1.74e+02j  3.24e+02-8.45e+01j  2.99e+01-2.16e+02j -3.50e-14-1.80e-14j  7.21e+01-5.46e+01j]]

    dft_hang:
    [[ 0.00e+00+0.00e+00j  1.02e+02+4.22e+01j  1.87e-14-2.13e-14j 1.02e+02+2.46e+02j  4.08e+02+7.49e-14j  1.02e+02-2.46e+02j -3.49e-14-3.55e-14j  1.02e+02-4.22e+01j]
     [ 0.00e+00+0.00e+00j  7.21e+01+5.46e+01j  1.78e-14-1.45e-14j 2.99e+01+2.16e+02j  3.24e+02+8.45e+01j  1.32e+02-1.74e+02j -1.74e-14-3.54e-14j  8.96e+01-1.24e+01j]
     [ 0.00e+00+0.00e+00j  5.98e+01+1.44e+02j  3.29e-14-2.58e-15j -1.44e+02+3.48e+02j  4.08e+02+4.08e+02j  3.48e+02-1.44e+02j 7.74e-15-7.75e-14j  1.44e+02+5.98e+01j]
     [ 0.00e+00+0.00e+00j  1.74e+02+2.16e+02j  5.85e-14-1.59e-14j -7.21e+01+6.67e+02j  9.00e+02+4.92e+02j  5.22e+02-4.20e+02j -3.41e-14-1.38e-13j  2.76e+02+2.99e+01j]
     [ 0.00e+00+0.00e+00j  3.06e+02+1.27e+02j  5.62e-14-4.97e-14j 3.06e+02+7.39e+02j  1.22e+03+3.25e-13j  3.06e+02-7.39e+02j -1.19e-13-1.21e-13j  3.06e+02-1.27e+02j]
     [ 0.00e+00+0.00e+00j  2.76e+02-2.99e+01j  2.42e-14-6.11e-14j 5.22e+02+4.20e+02j  9.00e+02-4.92e+02j -7.21e+01-6.67e+02j -1.37e-13-3.63e-14j  1.74e+02-2.16e+02j]
     [ 0.00e+00+0.00e+00j  1.44e+02-5.98e+01j  4.53e-15-4.01e-14j 3.48e+02+1.44e+02j  4.08e+02-4.08e+02j -1.44e+02-3.48e+02j -7.75e-14+6.47e-15j  5.98e+01-1.44e+02j]
     [ 0.00e+00+0.00e+00j  8.96e+01+1.24e+01j  1.19e-14-2.23e-14j 1.32e+02+1.74e+02j  3.24e+02-8.45e+01j  2.99e+01-2.16e+02j -3.50e-14-1.80e-14j  7.21e+01-5.46e+01j]]
    '''
    

    # Bước 4: Gọi hàm GaussianLP tạo bộ lọc thông thấp Gaussian
    H_uv = GaussianHP(10, P, Q)
    # print("H_uv: ", H_uv)
    '''
    H_uv: 
    [[0.15 0.12 0.1  0.08 0.08 0.08 0.1  0.12]
     [0.12 0.09 0.06 0.05 0.04 0.05 0.06 0.09]
     [0.1  0.06 0.04 0.02 0.02 0.02 0.04 0.06]
     [0.08 0.05 0.02 0.01 0.   0.01 0.02 0.05]
     [0.08 0.04 0.02 0.   0.   0.   0.02 0.04]
     [0.08 0.05 0.02 0.01 0.   0.01 0.02 0.05]
     [0.1  0.06 0.04 0.02 0.02 0.02 0.04 0.06]
     [0.12 0.09 0.06 0.05 0.04 0.05 0.06 0.09]]
    '''

    # Bước 5: Nhân ảnh sau khi DFT với ảnh sau khi lọc
    G_uv = np.multiply(dft_hang, H_uv)
    # print("G[u,v] = " + str(G_uv))
    '''
    G[u,v] = 
    [[ 0.00e+00+0.00e+00j  1.20e+01+4.96e+00j  1.78e-15-2.03e-15j 8.31e+00+2.01e+01j  3.14e+01+5.76e-15j  8.31e+00-2.01e+01j -3.32e-15-3.38e-15j  1.20e+01-4.96e+00j]
     [ 0.00e+00+0.00e+00j  6.21e+00+4.70e+00j  1.12e-15-9.12e-16j 1.46e+00+1.06e+01j  1.42e+01+3.72e+00j  6.43e+00-8.49e+00j -1.09e-15-2.23e-15j  7.71e+00-1.07e+00j]
     [ 0.00e+00+0.00e+00j  3.76e+00+9.08e+00j  1.29e-15-1.01e-16j -3.56e+00+8.60e+00j  8.08e+00+8.08e+00j  8.60e+00-3.56e+00j 3.03e-16-3.04e-15j  9.08e+00+3.76e+00j]
     [ 0.00e+00+0.00e+00j  8.49e+00+1.06e+01j  1.44e-15-3.91e-16j -7.18e-01+6.63e+00j  4.49e+00+2.46e+00j  5.20e+00-4.18e+00j -8.43e-16-3.40e-15j  1.35e+01+1.46e+00j]
     [ 0.00e+00+0.00e+00j  1.35e+01+5.58e+00j  1.11e-15-9.85e-16j 1.53e+00+3.68e+00j  0.00e+00+0.00e+00j  1.53e+00-3.68e+00j -2.35e-15-2.39e-15j  1.35e+01-5.58e+00j]
     [ 0.00e+00+0.00e+00j  1.35e+01-1.46e+00j  5.98e-16-1.51e-15j 5.20e+00+4.18e+00j  4.49e+00-2.46e+00j -7.18e-01-6.63e+00j -3.38e-15-8.96e-16j  8.49e+00-1.06e+01j]
     [ 0.00e+00+0.00e+00j  9.08e+00-3.76e+00j  1.77e-16-1.57e-15j 8.60e+00+3.56e+00j  8.08e+00-8.08e+00j -3.56e+00-8.60e+00j -3.04e-15+2.54e-16j  3.76e+00-9.08e+00j]
     [ 0.00e+00+0.00e+00j  7.71e+00+1.07e+00j  7.50e-16-1.40e-15j 6.43e+00+8.49e+00j  1.42e+01-3.72e+00j  1.46e+00-1.06e+01j -2.20e-15-1.13e-15j  6.21e+00-4.70e+00j]]
    '''
    

    # Bước 6:
    # Bước 6.1 Thực hiện biến đổi ngược DFT
    idft_cot = idft_hang = np.zeros((P, Q))
    # chuyển đổi DFT ngược theo P - theo cột
    for i in range(P):
        idft_cot[i] = IDFT1D(G_uv[i])
    # Chuyển đổi DFT ngược theo Q - theo hàng
    for j in range(Q):
        idft_hang[:, j] = IDFT1D(idft_cot[:, j])
        
    # print("idft_cot: ", idft_cot)
    # print("idft_hang: ", idft_hang)
    
    '''
    idft_cot:  
    [[ 4.50e+00 -2.42e+00  2.42e+00 -4.50e+00 -1.84e+00 -2.32e-01  2.32e-01 1.84e+00]
     [ 7.69e-01 -1.49e+00  1.49e+00 -7.69e-01  6.42e-01  8.10e-02 -8.10e-02 -6.42e-01]
     [ 7.82e-01 -4.37e-01  4.37e-01 -7.82e-01 -3.06e-01 -3.87e-02  3.87e-02 3.06e-01]
     [ 5.43e-01 -5.51e-01  5.51e-01 -5.43e-01  6.73e-03  8.50e-04 -8.50e-04 -6.73e-03]
     [ 3.11e-01 -3.15e-01  3.15e-01 -3.11e-01  3.86e-03  4.87e-04 -4.87e-04 -3.86e-03]
     [ 5.43e-01 -5.51e-01  5.51e-01 -5.43e-01  6.73e-03  8.50e-04 -8.50e-04 -6.73e-03]
     [ 7.82e-01 -4.37e-01  4.37e-01 -7.82e-01 -3.06e-01 -3.87e-02  3.87e-02 3.06e-01]
     [ 7.69e-01 -1.49e+00  1.49e+00 -7.69e-01  6.42e-01  8.10e-02 -8.10e-02 -6.42e-01]]

    idft_hang:  
    [[ 4.50e+00 -2.42e+00  2.42e+00 -4.50e+00 -1.84e+00 -2.32e-01  2.32e-01 1.84e+00]
    [ 7.69e-01 -1.49e+00  1.49e+00 -7.69e-01  6.42e-01  8.10e-02 -8.10e-02 -6.42e-01]
    [ 7.82e-01 -4.37e-01  4.37e-01 -7.82e-01 -3.06e-01 -3.87e-02  3.87e-02 3.06e-01]
    [ 5.43e-01 -5.51e-01  5.51e-01 -5.43e-01  6.73e-03  8.50e-04 -8.50e-04 -6.73e-03]
    [ 3.11e-01 -3.15e-01  3.15e-01 -3.11e-01  3.86e-03  4.87e-04 -4.87e-04 -3.86e-03]
    [ 5.43e-01 -5.51e-01  5.51e-01 -5.43e-01  6.73e-03  8.50e-04 -8.50e-04 -6.73e-03]
    [ 7.82e-01 -4.37e-01  4.37e-01 -7.82e-01 -3.06e-01 -3.87e-02  3.87e-02 3.06e-01]
    [ 7.69e-01 -1.49e+00  1.49e+00 -7.69e-01  6.42e-01  8.10e-02 -8.10e-02 -6.42e-01]]
    '''
    
    

    # Bước 6.2: Nhân phần thực ảnh sau khi biến đổi ngược với -1 mũ (x+y)
    g_array = np.asarray(idft_hang.real)
    P, Q = np.shape(g_array)
    g_xy_p = np.zeros((P, Q))
    for x in range(P):
        for y in range(Q):
            g_xy_p[x, y] = g_array[x, y] * np.power(-1, x + y)


    # print("Before (g_array): ", g_array)
    # print("After (g_xy_p): ", g_xy_p)
    
    '''
    Before (g_array):  
    [[ 4.50e+00 -2.42e+00  2.42e+00 -4.50e+00 -1.84e+00 -2.32e-01  2.32e-01 1.84e+00]
    [ 7.69e-01 -1.49e+00  1.49e+00 -7.69e-01  6.42e-01  8.10e-02 -8.10e-02 -6.42e-01]
    [ 7.82e-01 -4.37e-01  4.37e-01 -7.82e-01 -3.06e-01 -3.87e-02  3.87e-02 3.06e-01]
    [ 5.43e-01 -5.51e-01  5.51e-01 -5.43e-01  6.73e-03  8.50e-04 -8.50e-04 -6.73e-03]
    [ 3.11e-01 -3.15e-01  3.15e-01 -3.11e-01  3.86e-03  4.87e-04 -4.87e-04 -3.86e-03]
    [ 5.43e-01 -5.51e-01  5.51e-01 -5.43e-01  6.73e-03  8.50e-04 -8.50e-04 -6.73e-03]
    [ 7.82e-01 -4.37e-01  4.37e-01 -7.82e-01 -3.06e-01 -3.87e-02  3.87e-02 3.06e-01]
    [ 7.69e-01 -1.49e+00  1.49e+00 -7.69e-01  6.42e-01  8.10e-02 -8.10e-02 -6.42e-01]]
  
    After (g_xy_p):  
    [[ 4.50e+00  2.42e+00  2.42e+00  4.50e+00 -1.84e+00  2.32e-01  2.32e-01 -1.84e+00]
    [-7.69e-01 -1.49e+00 -1.49e+00 -7.69e-01 -6.42e-01  8.10e-02  8.10e-02 -6.42e-01]
    [ 7.82e-01  4.37e-01  4.37e-01  7.82e-01 -3.06e-01  3.87e-02  3.87e-02 -3.06e-01]
    [-5.43e-01 -5.51e-01 -5.51e-01 -5.43e-01 -6.73e-03  8.50e-04  8.50e-04 -6.73e-03]
    [ 3.11e-01  3.15e-01  3.15e-01  3.11e-01  3.86e-03 -4.87e-04 -4.87e-04 3.86e-03]
    [-5.43e-01 -5.51e-01 -5.51e-01 -5.43e-01 -6.73e-03  8.50e-04  8.50e-04 -6.73e-03]
    [ 7.82e-01  4.37e-01  4.37e-01  7.82e-01 -3.06e-01  3.87e-02  3.87e-02 -3.06e-01]
    [-7.69e-01 -1.49e+00 -1.49e+00 -7.69e-01 -6.42e-01  8.10e-02  8.10e-02 -6.42e-01]]
    '''
    

    # Bước 7: Rút trích ảnh kích thước MxN từ ảnh PxQ
    # Và đây ảnh cuối cùng sau khi lọc
    g_xy = g_xy_p[:shape[0], :shape[1]]
    # print("g_xy: ", g_xy)
    '''
    g_xy:  
    [[ 4.5   2.42  2.42  4.5 ]
    [-0.77 -1.49 -1.49 -0.77]
    [ 0.78  0.44  0.44  0.78]
    [-0.54 -0.55 -0.55 -0.54]]
    '''
    

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
    ax4.imshow(np.log(np.abs(dft_hang) + 1e-9), cmap='gray')  # cộng 1e-9 để tránh log(0)
    ax4.set_title('Bước 3: Phổ tần số ảnh sau khi DFT')
    ax4.axis('off')
    # Hiển thị phổ tần số của bộ lọc
    ax5.imshow(H_uv, cmap='gray')
    ax5.set_title('Bước 4: Phổ tần số Bộ lọc')
    ax5.axis('off')
    # Hiển thị phổ tần số của kết quả sau khi nhân Phổ tần số sau khi DFT
    # với bộ lọc
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
    
    plt.show()

    output_path = 'image/test_HPG_Result.tif'
    plt.savefig(output_path)
    print(f"Hình ảnh đã được lưu tại: {output_path}")






