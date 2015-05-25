package capstone.cs.holeinone;

import android.app.Notification;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.service.notification.NotificationListenerService;
import android.service.notification.StatusBarNotification;
import android.util.Log;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;

/**
 * Created by shinjiung on 15. 5. 17..
 */
public class NLService extends NotificationListenerService {
    public static final String EXTRA_TITLE = "android.title";
    private String TAG = this.getClass().getSimpleName();

    @Override
    public void onCreate() {
        super.onCreate();
        IntentFilter filter = new IntentFilter();
        filter.addAction("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_SERVICE_EXAMPLE");
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
    }

    @Override
    public void onNotificationPosted(StatusBarNotification sbn) {
        String s1 = sbn.getPackageName();
        String s2 = "com.kakao.talk";
        String s3 = "com.android.mms";
        if(s1.equals(s2))
        {
            Intent i = new  Intent("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE.Kakaotalk");
            i.putExtra("notification_kakao",sbn.getNotification().tickerText.toString());
            sendBroadcast(i);
        }
        if(s1.equals(s3)) {
            Intent i = new Intent("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE.Message");
            i.putExtra("notification_message", sbn.getNotification().tickerText.toString());
            sendBroadcast(i);
        }
    }

    @Override
    public void onNotificationRemoved(StatusBarNotification sbn) {
        Log.i(TAG,"********** onNOtificationRemoved");
        Log.i(TAG,"ID :" + sbn.getId() + "\t" + sbn.getNotification().tickerText.toString() +"\t" + sbn.getPackageName());
        Intent i = new  Intent("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE");
        sendBroadcast(i);
    }
}
