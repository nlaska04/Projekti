document.getElementById("year").textContent = new Date().getFullYear();
const button = document.getElementById('toggleButton');
        const para1 = document.getElementById('text');

     
 // Gjejmë elementin e kartës
const card = document.getElementById('about-card');

// Shto një event kur bejme hover me mouse mbi kartën
card.addEventListener('mouseover', () => {
    card.style.transform = 'scale(1.05)'; // Zmadhim të lehtë
    card.style.boxShadow = '0 6px 12px rgba(0, 0, 0, 0.3)'; // Hije më e theksuar
    card.style.backgroundColor = '#eef2f7'; // Ndryshim i sfondit
});

// Shto një event kur heqim mouse nga karta
card.addEventListener('mouseout', () => {
    card.style.transform = 'scale(1)'; // Kthehet në madhësinë fillestare
    card.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)'; // Hije origjinale
    card.style.backgroundColor = '#f9f9f9'; // Sfonda origjinale
});




// Funksion për të treguar ose fshehur formën
function toggleForm() {
    const form = document.getElementById('reservationForm');
    if (form.style.display === 'none' || form.style.display === '') {
        form.style.display = 'block'; // Trego formën
    } else {
        form.style.display = 'none'; // Fshih formën
    }
}

 