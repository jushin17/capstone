package capstone.cs.holeinone;

import android.app.Activity;
import android.app.NotificationManager;
import android.content.DialogInterface;
import android.app.AlertDialog;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.media.AudioManager;
import android.os.Bundle;
import android.speech.tts.TextToSpeech;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.TextView;
import android.widget.Toast;


import java.util.Locale;

/**
 * Created by shinjiung on 15. 5. 17..
 */
public class MainActivity extends Activity implements
        TextToSpeech.OnInitListener {

    public NotificationKakao nKakao;
    public NotificationMessage nMessage;
    public boolean kakaoReceiver = false;
    public boolean messageReceiver = false;
    private TextToSpeech tts;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_kakao);



        final CheckBox option1 = (CheckBox) findViewById(R.id.option1);
        final CheckBox option2 = (CheckBox) findViewById(R.id.option2);
        Button setupBtn = (Button) findViewById(R.id.setup_button);
        Button canReadBtn = (Button) findViewById(R.id.canReadBtn);
        setVolumeControlStream(AudioManager.STREAM_MUSIC);
        tts = new TextToSpeech(this,this);

        //use dialog for setting notification catch
        canReadBtn.setOnClickListener(new Button.OnClickListener() {
            public void onClick(View v) {

                //set dialog composition
                new AlertDialog.Builder(MainActivity.this)
                        .setTitle("알림접근 설정으로 이동")
                        .setMessage("알림 접근 창으로 이동하시려면 이동, 이미 완료되었다면 취소를 눌러주세요.")
                        .setPositiveButton("이동", new DialogInterface.OnClickListener()
                        {
                            //move to notification setting page
                            @Override
                            public void onClick(DialogInterface dialog, int which)
                            {
                                Intent intent = new Intent("android.settings.ACTION_NOTIFICATION_LISTENER_SETTINGS");
                                startActivity(intent);
                            }
                        })
                        .setNegativeButton("취소", new DialogInterface.OnClickListener()
                        {
                            @Override
                            public void onClick(DialogInterface dialog, int which)
                            {

                                dialog.dismiss();
                            }
                        })
                        .show();
            }
        });

        setupBtn.setOnClickListener(new Button.OnClickListener() {
            public void onClick(View v) {
                //activate BroadcastReceiver for TTS(text to speech) kakaotalk
                if(option1.isChecked()) {
                    if(!kakaoReceiver)
                    {
                        nKakao = new NotificationKakao();
                        IntentFilter filter = new IntentFilter();
                        filter.addAction("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE.Kakaotalk");
                        registerReceiver(nKakao,filter);
                        kakaoReceiver = true;
                    }
                }
                else {
                   onDestroyKakao();
                    kakaoReceiver = false;
                }
                //activate BroadcastReceiver for TTS(text to speech) message
                if(option2.isChecked() && messageReceiver == false) {
                    if(!messageReceiver) {
                        nMessage = new NotificationMessage();
                        IntentFilter filter = new IntentFilter();
                        filter.addAction("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE.Message");
                        registerReceiver(nMessage, filter);
                        messageReceiver = true;
                    }
                }
                else {
                    onDestroyMessage();
                    messageReceiver = false;
                }
                Toast.makeText(getApplicationContext(), "설정이 완료되었습니다.", Toast.LENGTH_SHORT).show();

            }
        });


    }

    protected void onDestroyKakao() {
        super.onDestroy();
        if (nKakao!=null) {
            unregisterReceiver(nKakao);
            nKakao=null;
        }
    }
    protected void onDestroyMessage() {
        super.onDestroy();
        if (nMessage!=null) {
            unregisterReceiver(nMessage);
            nMessage=null;
        }
    }


    //set TTS option
    @Override
    public void onInit(int status) {

        if (status == TextToSpeech.SUCCESS) {

            int result = tts.setLanguage(Locale.KOREAN);

            if (result == TextToSpeech.LANG_MISSING_DATA
                    || result == TextToSpeech.LANG_NOT_SUPPORTED) {
                Log.e("TTS", "This Language is not supported");
            } else {
                //speakOut();
            }

        } else {
            Log.e("TTS", "Initilization Failed!");
        }

    }

    private void speakOut(String text) {

        tts.speak(text, TextToSpeech.QUEUE_ADD, null);
    }

    public class NotificationKakao extends BroadcastReceiver {

        @Override
        public void onReceive(Context context, Intent intent) {
            String text = intent.getStringExtra("notification_kakao");
            speakOut(text);

        }
    }
    public class NotificationMessage extends BroadcastReceiver {

        @Override
        public void onReceive(Context context, Intent intent) {
            String text = intent.getStringExtra("notification_message");
            speakOut(text);
        }
    }



}