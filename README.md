# chip_counter

Chipzähler mit Vibrationsmotor und Touchscreen.

# BOM

Diese Materialien werden für das System benötigt:

| Device                         | Price  | Amount | Link                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------|--------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Raspberry PI 4B                | 66€    | 1      | [Amazon](https://www.amazon.de/Raspberry-Pi-ARM-Cortex-A72-Bluetooth-Micro-HDMI/dp/B07TC2BK1X/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=S10T9NMYUJLU&dib=eyJ2IjoiMSJ9.1UC1W5_zecYpKMlGIP7RLntnbY2FzwGMy1Miiy5XufC-c31GWVChQfnTsqR93XUYZXAFRSAn8F94lipW-hcpUEOu2EtuGqtMV-ELfLTizRyyDhaELjphD8D5gQfOed8uIu0Dm3IvZ37k9pel69QmW8cRXaSSpUuDzArWnIRDuTedcRmF1mon52yOm-X6oCxk3C5HRmOgruiFEq1if9Q0qzTQ3UrlvRO2OemAbPmBYZeAMlDJyJ97oc6R_ySvcggLmvv931uZIZkrGNlSNA0y-1cFzTowsu4KFZa9EqJLBo8.KmxMvNYHCx0sDy0MEZSJNWzJRwZ5ayMvOmIcgazh8pE&dib_tag=se&keywords=raspberry+pi+4&qid=1717599767&sprefix=raspberry+pi+4,aps,85&sr=8-5)                                                                                                 |
| 5" Touch Display               | 39,99€ | 1      | [Amazon](https://www.amazon.de/ELECROW-Touchscreen-Monitor-Raspberry-Kompatibel/dp/B0CZ6L8DNJ/ref=sr_1_10?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2IJR43BP3A1YJ&dib=eyJ2IjoiMSJ9._Lukts8pcMVVrcI5-RfLXp5QqfEwlRYuXCevrd4oNQVUFNWfjKSOIFSV1zRgW5eifA7sHJ2xzacg5_w8dq1GDNyV5Tsw1PgIb6EJCvi6l_jYdDvzKfNjY0QSy-JBR3tSe79uCfntfw6wyKbe7tSwKyHYgO1jLyDiEZLL7_i0exEEUobicsV_vqWZo4P020jOav6EE35JziGzS9rU5_7GTnJu0TX-5s5coiV4uWJqGDabDXrtNl72ZSkzfsgKOjCNWWZ3_wcHnDShu98V4Wfe8YbxT_f6KtotIE4TKW2A3Tw.Vq_RSJEl-uHmWJRMpqUBijQGOMg9URoRp1fz_v1f_xI&dib_tag=se&keywords=raspberry+pi+touch+display&qid=1717599903&sprefix=raspberry+pi+touch+display,aps,91&sr=8-10)                                                                      |
| Button Set                     | 7,25€  | 1      | [Amazon](https://www.amazon.de/RUNCCI-YUN-Momentanen-Druckschalter%EF%BC%8CMini-DruckTaster-Wasserdicht/dp/B0825RCZJS/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1MFY2S2JLO0L6&dib=eyJ2IjoiMSJ9.t5DhmddPxOJ7YF70kViIaEVbLRg4hk5xKL4nl_EquXliHHRenM8C_C5gsssK-oP6qeOoS4uHoyvGEU9TXklOqrMqfkn7lq4US1TlkK44D8bfmSXr4kxFISrmC-Pt2mbpYP1gJXlGbTQI1nAexv5MGwqU1ijx37IGRVZQjIAodzTTM0grkz9zsvNdpvf35ehkAmwexN3e5CilEw-PsndEkvgdFBY_t_NWlQRUr0fs2P1-LAOeBQKCy_2uehuBtafAoW1tbowHdCeDmqXNP6Zw6e8NMiUxrTxV9Z0rOxcTwns.JkYH_LyI5KfRWBJBIAxUoF8EJYM01C6TKA63ZWPpAvs&dib_tag=se&keywords=raspberry+pi+button&qid=1717600059&sprefix=raspberry+pi+b,aps,573&sr=8-1)                                                                  |
| Schlüsselschalter              | 9,03€  | 1      | [Amazon](https://www.amazon.de/Create-idea-Edelstahl-Vollmetall-Verriegelnder-Edelstahl-Metall-Schl%C3%BCsselschalter/dp/B0D35B4ZCB/ref=sr_1_6?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1NFA1ZM8CSCQP&dib=eyJ2IjoiMSJ9.V5_-h8aNh87dyKb46Rx8HuQMcVPZ9XjQh3bxBR6o0Bk3sn1HcDGx4Uaa3Vh64KfDSJeJb49JPDRn0Wg8wggksEVoThaEwlbiVWN8J5y3sT5wfS4nhmBPEFYKFkFXyqX_y9_nFIn-oYVSNfBLWBoXKQaXGxpTtNi3MH-89vDLuZU1et1Pngq-Al2TwZhLpjgrOBdGHRML9H45Bzut3zgysJKjdTw1BdU3jzgUl4cECTYhhpVgiZhVCq698QH_BC__gXvhCuzUbsQXInq43Lb_sLefIzRxBpue9k53jUpQO9Q.ffEUV-J6x8xeW18fP2unO7B0Ffk-hMWiStZBbhY8Phc&dib_tag=se&keywords=schl%C3%BCsselschalter+3+positionen&qid=1717600822&sprefix=schl%C3%BCsselschalter+3+positionen+,aps,75&sr=8-6&th=1)          |
| Infrarot Sender und Empfänger  | 6,99€  | 1      | [Amazon](https://www.amazon.de/BOJACK-Infrarot-Emitter-IR-lampe-Empf%C3%A4ngerdiode-Infrarot-Emissions-Empf%C3%A4ngerr%C3%B6hre/dp/B08Y6Y9S5Q/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1G44VE73ZOEJS&dib=eyJ2IjoiMSJ9.iuzWWHHoqyO63tQV84g0reX71GGWwpDS22-BIh-qwsKroK_77tS2CrTuwNGgWs41lX33iZFagdwLr6kJpDbsFc2XN1K8fuLPSGzqHSYkpHpCRO8IH4QRamC2vDFlHE-mK1rYP6HQnHCEL7L6T1UaChL4jApzd98WmI5n0Na9o_RQnsfKRT9Il184KRz0ynY_mfgrr_-iAkzRPh0nzzx9-WQQ9xpIR0lnqnzaWPxsxctjIM2Xfo7wTvV5w-_QoROvqPmS3CeRKeEdLKrUHI31yz2ud4vjDWjfoz_ql1k8K5w.eWHp2PYG6b1pyq7v3GPafsTXTUPh5b5SE9zkLxYQaRo&dib_tag=se&keywords=raspberry+pi+infrared+beam&qid=1717601249&sprefix=raspberry+pi+infrared+beam,aps,212&sr=8-1)                       |
| GPIO Breakoput Board           | 14,95€ | 1      | [Amazon](https://www.amazon.de/FREENOVE-Breakout-Raspberry-Terminal-Status/dp/B0BFB618CJ/ref=sr_1_4?crid=1W7LU3L7EYH15&dib=eyJ2IjoiMSJ9.WyV1zZpULPT770-AF3VQwANkxJbGxllTvTzcbHFWVLCUoEkTEDUsRwHVVfWH9vhGsrtklw4OIUJ6woSuPTXPDs0o3pfh8q6iH3FB2TG87d8Cv7kXQxBcSJDK8d9wlgHUO5mUanLJ_6EsDfKqhDN4kTmwJ1DJr8Rmk51fqSs6--2BtpMwA_GO0Mq3F2DSQjEon7BtyhJ0ysGHm6-7OtbpPy6v4tdelMF7G8amQfYset3faxtWsGLXwFLUGrkxjiZsP2T8keNF8gMv9pgS3G4Vge8NMiUxrTxV9Z0rOxcTwns.BtHoSEx60asZSi_2KHzPfpsM5RMt0AtQKoybmRX3NZg&dib_tag=se&keywords=raspberry+pi+4+gpio+breakout&qid=1717601478&sprefix=raspberri+pi+4+gpio+break,aps,172&sr=8-4)                                                                                                                      |
| Jumper Kabel                   | 5,94€  | 1      | [Amazon](https://www.amazon.de/Female-Female-Male-Female-Male-Male-Steckbr%C3%BCcken-Drahtbr%C3%BCcken-bunt/dp/B01EV70C78/ref=sr_1_6?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1H8AK2O3YGVRQ&dib=eyJ2IjoiMSJ9.YkJGGaT6C6WFjyXfDkQJR983TvUgVBGHgrCw5goe9P4P-pORv5R7vYJxtH06f5697bmLJpB0-9Eg0EjgmKiB0ice_MQIKqi_g1QlW7KXxMPbHV3GLc8NpFDUp1_ZQtW9nz1ptqky65FR9S4_5TtQJ4y3-hAQuRB1uml9m4jjyd6-_8MExrR5MIEJir1pbX7uf5sqp7xlHqRrcUAZuSeykHO3vtvsGwdludpVNv35Rkyd7II8e7EJJOIMVDKXyBguUHVQKwAaOS9RCAe8auTrogISqlh2irb5_45y4YAJmvk.42vu6HdKJ5ELTvL-9KlYiqz-mZVL_9MQ1PGIholPmGk&dib_tag=se&keywords=raspberry+pi+4+jumper+wires&qid=1717601593&sprefix=raspberry+pi+4+jumper+wires,aps,278&sr=8-6)                                         |
| Elektrische Bauteile           | 18,69€ | 1      | [Amazon](https://www.amazon.de/Elektronisches-Bauelemente-Set-Transistor-Elektrolytkondensatoren-Widerst%C3%A4nde-Bauelemente-Sortiment/dp/B09GVZ4STX/ref=sr_1_9?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3A3X7BHYX45UK&dib=eyJ2IjoiMSJ9.RIqZfiEtLVPyPzeiMSLI2vdKb11EZkSW9Ck6AIN6VkuMOzjVytj5co6LVB11_iVwwbLSuTfc7ZG-UOwMEeq1LZBHukEeb4XKVpEolJleRhZ_eDf4ltLqXJDpL5eF5-LcQFZDnmignOPCLz_uZoWomWeSGijwAtrfBcnIPBecw-ccL9KjyGL-3_kOPY-m4MTKLOflCy6iqT6GJqFUDss1XRMrcWJfqGygWUn-f7qAvflpm262uTrPg2Sbfiac5N0Tpl2NOcOfd7RrUcOTsTP1jfQFSQaIxtcFGAC-_ZO_m_M._wRx5pvgc_MqEr537PVj94RuOCp-YxHWmDdsSPe-Krc&dib_tag=se&keywords=widerstand+und+kapazit%C3%A4t+set&qid=1717601722&sprefix=widerstand+und+kapazit%C3%A4t+set,aps,152&sr=8-9) |
| 12V Vibrationsmotor (?)        | 17,99€ | 1      | [Amazon](https://www.amazon.de/ICQUANZX-Gleichstrom-Vibrationsmotor-drehmomentstarke-Vibrationsmotoren-eisenrotierenden/dp/B0824V4M4R/ref=sr_1_20?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3QE7G3FHDL5ZQ&dib=eyJ2IjoiMSJ9.h-xg7aFbO--_CAddeJKIJr4w2Z--hfHIHXim1VNWlt_INQ5uv_vjsnclQk1n-D-qvYCnIxtWufPXq2MT2CQ4bvwNHaogQyN6dW6vws0aaxnNRlHcK-O-CNZN4UtQElqMbhkowthgiKYw9_zazOApIBdNnaiiH8kGW8AsYQ8wmDzZoVRz5meWhoLeyxiSB2X42p_IEBbezhaB-Cph6dC1K226tE75hSxvjpOA-2LsE5hYE-F2wQvEasd04-u1dQbuH6yPB4TtgnBNooRNqV538yoM2F_gWyOTCie2aaU_AHo.f9tbRIZlHIC9JQwQQjoc1XhZ3EV2C5daqQzF_aBWdWk&dib_tag=se&keywords=elektromotor+r%C3%BCttelplatte&qid=1717601914&sprefix=elektromotor+r%C3%BCttelplatte,aps,125&sr=8-20)                     |
| PWM Drehzahl Steller           | 7,99€  | 1      | [Amazon](https://www.amazon.de/WayinTop-Drehzahlsteller-Geschwindigkeitsregler-Niederspannungs-Steuerungsmodul/dp/B07ZPRM23X/ref=pd_bxgy_d_sccl_1/259-2419948-4853506?pd_rd_w=NoFqN&content-id=amzn1.sym.d6531279-1f86-4ae1-b1f7-8ab9db04b1a0&pf_rd_p=d6531279-1f86-4ae1-b1f7-8ab9db04b1a0&pf_rd_r=F1CQA05XE0QS9KPERNR6&pd_rd_wg=6BWMA&pd_rd_r=55bac055-6606-44a8-a670-1c25cd31f45a&pd_rd_i=B07ZPRM23X&psc=1)                                                                                                                                                                                                                                                                                                                          |
| 12V Netzteil                   | 8,90€  | 1      | [Amazon](https://www.amazon.de/Spannungswandler-Netzteil-f%C3%BCr-LED-Streifen-220/dp/B01G0Q3RWU/ref=pd_bxgy_d_sccl_1/259-2419948-4853506?pd_rd_w=GxAxn&content-id=amzn1.sym.d6531279-1f86-4ae1-b1f7-8ab9db04b1a0&pf_rd_p=d6531279-1f86-4ae1-b1f7-8ab9db04b1a0&pf_rd_r=CHF2AV4AG6B50NWTJRZM&pd_rd_wg=GG3MY&pd_rd_r=08aa7d9f-4108-4518-9d08-2113a204514c&pd_rd_i=B01G0Q3RWU&psc=1)                                                                                                                                                                                                                                                                                                                                                      |
| Doppelrelais 5V steuerspannung | 11,78€ | 1      | [Amazon](https://www.amazon.de/dp/B07QYLN6LD?psc=1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

# Aufbau
Das System muss wie folgt aufgebaut werden. Die genaue Pinbelegung kann aus der [Config](assets/config.toml)
entnommen werden.
![](schematics/chip_counter.png)

# Bedienungsanleitung

Das System ist designt um Chips zu zählen. Da es zwei verschiedene Arten von
Chips gibt, werden zwei verschiedene Auffangbehältnisse eingerichtet, welche das 
System mit zwei Motoren unabhängig voneinander ansteuert, damit diese Vibrieren und
die Chips in den Zählschlitz befördern. Dort befindet sich ein Infrarotsensor, welcher 
die Chips je nach Farbe zählt und auf dem Display anzeigt. Am Einwurf der Auffangbehälter 
wird auch ein Infrarotsensor montiert, damit die Vibration automatisch eingeleitet wird.

## Bedienung
Das System inkorporiert mehrere Steuereinheiten um das Verhalten zu modifizieren.

* Motor manuell starten (`Pin 10`)
* Zähler auf der Hauptseite zurücksetzen (`Pin 22`)
* Hauptansicht anzeigen (`Pin 27`)
* Adminansicht anzeigen (`Pin 17`)

Zusätzlich können in der Adminansicht über den Touchscreen Einstellungen vorgenommen werden.

## Adminansicht

In der Adminansicht lassen sich die Daten des ganzen Tages wiederfinden, inklusive der Zählungen 
mit Faktor inkludiert. Die Daten werden stündlich in einem Barchart angezeigt, um Informationen
über die tägliche Auslastung zu erhalten. 

## Einstellungen

Durch die Adminansicht kann man auch in die Einstellungen (`Settings` oben rechts) gelangen.
In den Einstellungen kann die Motorlaufzeit und der Faktor eingestellt werden.
Zusätzlich kann man dort auch alle Zähler zurücksetzen und das Programm schließen.