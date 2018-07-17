<?php

/**
 * curl文件表单上传
 * @author Bill
 */

/**
 * htppCurl表单上传文件
 * @param $src
 * @param string $urlRoute
 * @return bool|mixed
 */
function curlSendFile(CURLFile $file, $url = '', $key = "cc123456")
{
    if ($file == null || $url == '')
        return false;
    $post_data = [];
    $post_data["file"] = $file;
    $post_data["key"] = $key;
    return postCurl($url, $post_data);
}

/**
 * CurlPost请求
 * @param $url
 * @param $data
 * @return mixed
 * @author Bill
 */
function postCurl($url, $data)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    $output = curl_exec($ch);
    curl_close($ch);
    return $output;
}

//Demo :
$url = "http://127.0.0.1:3000/upload";
$res = curlSendFile(new CURLFile('DX_1957_M_20131024_DX22050.dcm'), $url);
var_dump($res);
