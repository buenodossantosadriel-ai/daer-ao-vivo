curl -s https://www.daer.rs.gov.br/cameras-de-monitoramento -A "Mozilla" | grep -o "ptz_[a-z_0-9]*" | sort -u

echo "--- tentando JS do site ---"
curl -s https://www.daer.rs.gov.br/cameras-de-monitoramento -A "Mozilla" | grep -o "codigo-camera/[^\"']*" | sort -u
