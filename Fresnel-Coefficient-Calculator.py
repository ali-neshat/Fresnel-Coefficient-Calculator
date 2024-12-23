import numpy as np
import matplotlib.pyplot as plt

# ضریب شکست محیط اول و دوم
n1 = 1.0  # ضریب شکست محیط اول (هوا)
n2 = 1.55  # ضریب شکست محیط دوم (مثلاً شیشه)

# تعریف زوایای برخورد از 0 تا 90 درجه
angles = np.linspace(0, 90, 100)
angles_rad = np.radians(angles)  # تبدیل به رادیان

# محاسبه زاویه شکست با استفاده از قانون اسنل
theta_t = np.arcsin(n1 * np.sin(angles_rad) / n2)

# محاسبه ضرایب بازتاب فرنل
Rs = ((n1 * np.cos(angles_rad) - n2 * np.cos(theta_t)) /
      (n1 * np.cos(angles_rad) + n2 * np.cos(theta_t)))**2
Rp = ((n2 * np.cos(angles_rad) - n1 * np.cos(theta_t)) /
      (n2 * np.cos(angles_rad) + n1 * np.cos(theta_t)))**2

# محاسبه ضرایب عبور
Ts = 1 - Rs
Tp = 1 - Rp

# رسم نمودار
plt.figure(figsize=(8, 6))
plt.plot(angles, Rs, label="Rs (s-polarization)", color="blue")
plt.plot(angles, Rp, label="Rp (p-polarization)", color="red")
plt.plot(angles, Ts, '--', label="Ts (s-polarization)", color="blue")
plt.plot(angles, Tp, '--', label="Tp (p-polarization)", color="red")
plt.xlabel('angle of incidence (degrees)')
plt.ylabel('Fresnel coefficient')
plt.title("Fresnel's reflection and transmission coefficients according to the angle of incidence")
plt.legend()
plt.grid(True)
plt.show()