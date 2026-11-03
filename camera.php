<?php
$cam = $_GET['cam'] ?? 'ptz_santa_maria';

if ($cam === 'ptz_passo_fundo') {
    $url = "https://daer.kopp.com.br/ftp/imagem.php?id=Passo_Fundo";
} else {
    $url = "https://daer.kopp.com.br/sistrak-base-010/rs/importacao/camera-importador-operacao-registro/codigo-camera/$cam";
}

$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_REFERER => 'https://www.daer.rs.gov.br/cameras-de-monitoramento',
    CURLOPT_USERAGENT => 'Mozilla/5.0',
]);
$data = curl_exec($ch);
curl_close($ch);
header("Content-Type: image/jpeg");
echo $data;
