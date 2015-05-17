package capstone.cs.holeinone;

import android.content.Intent;
import android.content.IntentFilter;
import android.service.notification.NotificationListenerService;
import android.service.notification.StatusBarNotification;
import android.util.Log;

import java.text.DateFormat;
import java.text.SimpleDateFormat;

/**
 * Created by shinjiung on 15. 5. 17..
 */
public class NLService extends NotificationListenerService {

    private String TAG = this.getClass().getSimpleName();
    //private NLServiceReceiver nlservicereciver;
    @Override
    public void onCreate() {
        super.onCreate();
        //nlservicereciver = new NLServiceReceiver();
        IntentFilter filter = new IntentFilter();
        filter.addAction("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_SERVICE_EXAMPLE");
        //registerReceiver(nlservicereciver,filter);
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        //unregisterReceiver(nlservicereciver);
    }

    @Override
    public void onNotificationPosted(StatusBarNotification sbn) {

        DateFormat df = new SimpleDateFormat("hh:mm");
        String time = df.format(sbn.getPostTime());
        Log.i(TAG, "**********  onNotificationPosted");
        Log.i(TAG,"ID :" + sbn.getId() + "\t" + sbn.getNotification().tickerText.toString() + "\t" + time);
        Intent i = new  Intent("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE");
        i.putExtra("notification_event",sbn.getNotification().tickerText.toString());
        sendBroadcast(i);

    }

    @Override
    public void onNotificationRemoved(StatusBarNotification sbn) {
        Log.i(TAG,"********** onNOtificationRemoved");
        Log.i(TAG,"ID :" + sbn.getId() + "\t" + sbn.getNotification().tickerText.toString() +"\t" + sbn.getPackageName());
        Intent i = new  Intent("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE");
        // i.putExtra("notification_event","onNotificationRemoved :" + sbn.getPackageName() + "\n");

        sendBroadcast(i);
    }
/*
    class NLServiceReceiver extends BroadcastReceiver{

        @Override
        public void onReceive(Context context, Intent intent) {
            if(intent.getStringExtra("command").equals("clearall")){
                NLService.this.cancelAllNotifications();
            }
            else if(intent.getStringExtra("command").equals("list")){
                Intent i1 = new  Intent("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE");
                i1.putExtra("notification_event","=====================");
                sendBroadcast(i1);
                int i=1;
                for (StatusBarNotification sbn : NLService.this.getActiveNotifications()) {
                    Intent i2 = new  Intent("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE");
                    i2.putExtra("notification_event",i +" " + sbn.getPackageName() + "\n");
                    sendBroadcast(i2);
                    i++;
                }
                Intent i3 = new  Intent("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE");
                i3.putExtra("notification_event","===== Notification List ====");
                sendBroadcast(i3);

            }

        }
    }
*/
}
