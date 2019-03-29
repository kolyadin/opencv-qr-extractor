<?php

use Zxing\QrReader;

require_once __DIR__ . '/vendor/autoload.php';

$found = $notFound = 0;

foreach (scandir(__DIR__ . '/samples') as $file) {
    if (!preg_match('!\.(jpeg|png)\z!', $file)) continue;

    $filepath = __DIR__ . '/samples/'. $file;

    $qrcode = new QrReader($filepath, QrReader::SOURCE_TYPE_FILE, false);
    $result = $qrcode->text();

    if (false !== $result) {
        $found++;
        echo "QR found ($found)", PHP_EOL;
    } else {
        $notFound++;
        echo "QR not found ($notFound)", PHP_EOL;
    }
}

echo "===Summary==", PHP_EOL;
echo "Fast found: ", $found, PHP_EOL;
echo "Not found: ", $notFound, PHP_EOL;
