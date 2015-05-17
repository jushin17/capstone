package capstone.cs.holeinone;

import java.io.IOException;
import java.io.OutputStream;
import java.util.UUID;

import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import android.view.View.OnClickListener;

public class Bluetooth extends Activity {
	TextView header;
    Button discoverDevicesBtn;
    Button sendMsgBtn;
    Button closeBtn;
    EditText sendTxt;
    BluetoothAdapter btAdapter;
    BluetoothSocket btSocket;
    private static String btAdress = "00:10:60:D1:95:CD";
    private static final UUID MY_UUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");
    private OutputStream out;
    public BluetoothDevice device;
    private Boolean CONNECTED = false;
    
	/** Called when the activity is first created. */
	@Override
	public void onCreate(Bundle savedInstanceState) {
	    super.onCreate(savedInstanceState);
	    setContentView(R.layout.activity_bluetooth);
	    // TODO Auto-generated method stub
	  //init layout parameters        
        header = (TextView) findViewById(R.id.text1);
        discoverDevicesBtn = (Button) findViewById(R.id.discBtn);
        sendMsgBtn = (Button) findViewById(R.id.sendButton);
        closeBtn = (Button) findViewById(R.id.closeButton);
        sendTxt = (EditText) findViewById(R.id.editText1);
        discoverDevicesBtn.setOnClickListener(discoverDeviceListener);
        sendMsgBtn.setOnClickListener(sendMsgListener);
        //closeBtn.setOnClickListener(l);
        //init bluetooth
        btAdapter = BluetoothAdapter.getDefaultAdapter();
        if (btAdapter.isEnabled()) {
            Toast.makeText(this, "Bluetooth state:" + btAdapter.getState() + " Ok!", Toast.LENGTH_LONG).show();
        } else {
            Toast.makeText(this, "Bluetooth state:" + btAdapter.getState() + " Not ok!", Toast.LENGTH_LONG).show();
        }

    }

    private Button.OnClickListener discoverDeviceListener = new Button.OnClickListener() {@Override
        public void onClick(View v) {
            if (!CONNECTED) {
                device = btAdapter.getRemoteDevice(btAdress);
                header.append("\nRemote device: " + device.getName());
                try {
                    btSocket = device.createRfcommSocketToServiceRecord(MY_UUID);
                } catch (Exception e) {
                                    }
                header.append("\n createRfcommsockettoservice! ");
                btAdapter.cancelDiscovery();
                try {
                    btSocket.connect();
                    CONNECTED = true;
                    header.append("\n btSocket Created!");
                } catch (IOException e) {
                    Toast.makeText(getApplicationContext(), "Could not connect to socket", Toast.LENGTH_LONG);
                    try {
                        btSocket.close();
                    } catch (Exception b) {}
                }
            }

        }
    };


    private Button.OnClickListener sendMsgListener = new Button.OnClickListener() {@Override
        public void onClick(View v) {
            if (CONNECTED) {
                try {
                    out = btSocket.getOutputStream();
                    String msg = sendTxt.getText().toString();
                    byte[] msgBffr = msg.getBytes();
                    out.write(msgBffr);
                    Toast.makeText(getApplicationContext(), "Message sent", Toast.LENGTH_LONG).show();
                } catch (Exception a) {
                    Toast.makeText(getApplicationContext(), "Could not send msg", Toast.LENGTH_LONG).show();
                }
            } else {
                Toast.makeText(getApplicationContext(), "cant send msg, not connected", Toast.LENGTH_LONG).show();
            }

        }
    };
	

}
