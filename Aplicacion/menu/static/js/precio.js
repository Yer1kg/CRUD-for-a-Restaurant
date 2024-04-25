document.addEventListener("DOMContentLoaded", function () {
    var precioInput = document.getElementById("numprecio");

    // Agrega el símbolo del euro cuando el campo pierde el foco (blur)
    precioInput.addEventListener("blur", function () {
        var valor = this.value.trim();
        if (valor && !valor.endsWith("€")) {
            this.value = valor + "€";
        }
    });

    // Elimina el símbolo del euro cuando el campo recibe el foco (focus)
    precioInput.addEventListener("focus", function () {
        var valor = this.value.trim();
        if (valor.endsWith("€")) {
            this.value = valor.slice(0, -1);
        }
    });

    // Elimina el símbolo del euro antes de enviar el formulario
    var form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", function () {
            precioInput.value = precioInput.value.replace("€", "").trim();
        });
    }
});
