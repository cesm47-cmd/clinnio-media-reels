/* BORRADOR D-055 · NO PUBLICAR. Va al final de app.js de la lista de espera, después del código actual.
   Falta: el ID del píxel (lo da César cuando cree la cuenta publicitaria) y el ID del sitio en Umami. */
(function(){
  var PIXEL_ID = 'PENDIENTE_CESAR';           // no inventar; queda vacío hasta que César lo dé
  var CLAVE = 'clinnio_cookies_meta';         // 'si' o 'no', guardado solo en este navegador

  function cargarPixel(){
    if (window.fbq || PIXEL_ID === 'PENDIENTE_CESAR') return;
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
    n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
    document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('set', 'autoConfig', false, PIXEL_ID);  // sin captura automática de botones ni campos
    fbq('init', PIXEL_ID);                      // sin coincidencia avanzada: no se envían correo ni teléfono
    fbq('track', 'PageView');
  }

  // Aviso de cookies: el píxel no se carga hasta que la persona acepta (regla 13)
  var aviso = document.getElementById('aviso-cookies');
  var eleccion = localStorage.getItem(CLAVE);
  if (eleccion === 'si') cargarPixel();
  else if (eleccion === null && aviso) aviso.hidden = false;
  document.getElementById('cookies-si').addEventListener('click', function(){
    localStorage.setItem(CLAVE,'si'); aviso.hidden = true; cargarPixel();
  });
  document.getElementById('cookies-no').addEventListener('click', function(){
    localStorage.setItem(CLAVE,'no'); aviso.hidden = true;
  });
  document.getElementById('cookies-cambiar').addEventListener('click', function(e){
    e.preventDefault(); localStorage.removeItem(CLAVE); aviso.hidden = false;
  });

  // Registro: evento estándar Lead sin parámetros ni campos del formulario (regla 11)
  window.clinnioRegistroEnviado = function(){
    if (window.fbq) fbq('track', 'Lead');
    if (window.umami) umami.track('registro');   // Umami ya guarda la fuente UTM de la visita
  };
})();
/* En app.js actual, dentro de .then(function(){ ... }) del envío, agregar una línea:
     if (window.clinnioRegistroEnviado) window.clinnioRegistroEnviado();
   En index.html, dentro de <head>, antes de </head> (analítica sin cookies, mide visitas por UTM):
     <script defer src="https://cloud.umami.is/script.js" data-website-id="PENDIENTE_CESAR"></script>
   En index.html, antes de <script src="app.js">, el aviso de cookies:
     <div id="aviso-cookies" class="aviso" role="region" aria-label="Cookies" hidden>
       <p>Usamos cookies de Meta para saber si nuestros anuncios funcionan. <a href="#datos">Más información</a></p>
       <button type="button" id="cookies-si">Aceptar</button>
       <button type="button" id="cookies-no">Rechazar</button>
     </div>
   Y en el <footer>: <a href="#" id="cookies-cambiar">Cookies</a> */
