The choice of D0 depends on the desired filtering effect:

Smaller D0: More aggressive filtering, resulting in stronger edge enhancement or blurring.
Larger D0: Less aggressive filtering, resulting in a more subtle effect.
By carefully selecting the D0 value, you can tailor the filter to specific image processing tasks, such as noise reduction, edge detection, or image sharpening

It defines the boundary between low-frequency and high-frequency components in the frequency domain.

However, the way D0 is used to shape the filter's response differs among these filter types:

Ideal Filter:

Has a sharp cutoff at D0.
All frequencies below D0 are passed, and all frequencies above D0 are blocked.
This ideal filter is not physically realizable due to its abrupt transition.   
Gaussian Filter:

Uses a Gaussian function to smoothly transition between the passband and stopband.
D0 determines the width of the transition region. A smaller D0 results in a sharper transition, while a larger D0 results in a smoother transition.
Butterworth Filter:

Provides a more gradual transition between the passband and stopband compared to the ideal filter.
The filter's order n influences the steepness of the transition. A higher order n results in a sharper transition.
D0 still defines the approximate cutoff frequency, but the transition is smoother.