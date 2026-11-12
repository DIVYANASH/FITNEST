// Animate result numbers when the dashboard loads.
document.querySelectorAll(".counter").forEach((element) => {
    const target = Number(element.dataset.value);
    const decimals = Number(element.dataset.decimals || 0);
    const duration = 900;
    const start = performance.now();

    function animate(now) {
        const progress = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        const value = target * eased;
        element.textContent = value.toFixed(decimals);

        if (progress < 1) {
            requestAnimationFrame(animate);
        }
    }

    requestAnimationFrame(animate);
});

// A simple visual indicator for the BMI value (not a medical score).
const bmiNumber = document.querySelector(".bmi-number");
const bmiMeter = document.getElementById("bmiMeter");

if (bmiNumber && bmiMeter) {
    const bmi = Number(bmiNumber.dataset.value);
    const width = Math.max(3, Math.min((bmi / 40) * 100, 100));
    setTimeout(() => {
        bmiMeter.style.width = width + "%";
    }, 100);
}

// Prevent accidental double submission.
const form = document.getElementById("fitnessForm");
if (form) {
    form.addEventListener("submit", () => {
        const button = form.querySelector("button[type='submit']");
        button.disabled = true;
        button.textContent = "Calculating...";
    });
}
