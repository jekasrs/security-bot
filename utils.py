import cv2
import numpy as np

backSub = cv2.createBackgroundSubtractorMOG2(50, 16, True)


def is_detected(frame):
    # шаг 1: получить изображение
    # шаг 2: вычитание фона
    fg_mask = backSub.apply(frame)

    # шаг 3: бинаризация маски
    _, mask_thr = cv2.threshold(fg_mask, 100, 255, 0)  # с тенями

    # шаг 4: исключение мелкого шума
    kernel_open = np.ones((5, 5), np.uint8)
    mask_open = cv2.morphologyEx(mask_thr, cv2.MORPH_OPEN, kernel_open)

    # шаг 5: исключение мелких областей
    kernel_close = np.ones((9, 9), np.uint8)
    mask_close = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel_close)

    # шаг 6: поиск контуров
    contours, _ = cv2.findContours(mask_close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # шаг 7: исключение контуров малой площади
    area_threshold = 100
    contours_sel = [cnt for cnt in contours if cv2.contourArea(cnt) > area_threshold]

    # шаг 8: расчет площади контуров
    total_area = 0
    for cnt in contours_sel:
        total_area += cv2.contourArea(cnt)
    rel_area = total_area / (frame.shape[0] * frame.shape[1]) * 100

    # шаг 9: проверка движения в кадре
    motion_threshold = 0.5

    return rel_area > motion_threshold
