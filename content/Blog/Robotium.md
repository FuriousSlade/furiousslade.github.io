Title:Robotium只有apk情况下的代码片段。
Date:2015-05-15 15:40
Category:Blog
Tags:Android,Robotium
Summary:记录下Robotium只有apk情况下的如何使用的代码片段。

	package com.example.tt.test;
	
	import com.robotium.solo.Solo;
	import android.app.Activity;
	import android.provider.UserDictionary.Words;
	import android.test.ActivityInstrumentationTestCase2;
	import android.view.View;
	
	
	@SuppressWarnings("rawtypes")
	public class TestVs extends ActivityInstrumentationTestCase2{
		
		public Solo solo;
		
		public Activity activity;
		private static Class<?> launchActivityClass;
		private static String mainActiviy = "com.paobao.verysercall.activity.LogoActivity";
	
		private static String packageName = "com.paobao.verysercall";
		
		static{
			
		try{
			
		launchActivityClass = Class.forName(mainActiviy);
			
		}catch (ClassNotFoundException e){
		throw new RuntimeException(e);
		}
			
		}
	
		
		@SuppressWarnings({ "unchecked", "deprecation" })
		public TestVs() {
	
			super(packageName, launchActivityClass);
	
		}
		
		@Override
		protected void setUp() throws Exception {
	
		super.setUp();
	
		this.activity = this.getActivity();
	
		this.solo = new Solo(getInstrumentation(), getActivity());
	
		}
	
		/*
		public void testCountryCode() throws Exception {
			 solo.waitForText("快速注册", 1, 1000);
			 solo.clickOnText("国家和地区");
			 solo.clickOnText("+30");
			 View view = null;
			 view = solo.getView("android:id/action_bar");
			 solo.waitForView(view);
			 boolean foundcode = solo.searchText("+30");
			 assertTrue("Country code is not found",foundcode);
			 solo.clickOnText("+30");
			 solo.clickOnText("+86");
			 view = solo.getView("android:id/action_bar");
			 foundcode = solo.searchText("+86");
			 assertTrue("Country code is not found",foundcode);
		}
		
	
		public void testLogInCaseOne() throws Exception{
			solo.waitForText("下一步",1, 1);
			solo.clickOnEditText(0);
			solo.enterText(0, "73761000864");
			solo.clickOnText("下一步");
			boolean findToast = solo.waitForText("验证码发送失败！");
			assertTrue("手机号码格式错误，不该发送验证码。",findToast);
			
		}
	
	
		public void testLogInCaseTwo() throws Exception{
			solo.waitForText("下一步",1, 1);
			solo.clickOnEditText(0);
			solo.enterText(0, "13761000864");
			solo.clickOnText("下一步");
			boolean findToast = solo.waitForText("短信验证码发送成功");
			assertTrue("验证码发送失败",findToast);
			boolean tmpText = solo.waitForText("重新获取");
			assertTrue(tmpText);
			solo.enterText(0, "1234");
			solo.clickOnText("下一步");
			solo.waitForText("通话记录");
			
		}
		*/
		
		public void testMePage() throws Exception{
			solo.clickOnText("我");
			solo.waitForText("我", 2, 10);
			solo.waitForText("剩余时间");
			solo.waitForText("用户");
			solo.waitForText("充值");
			solo.waitForText("面对面分享");
			solo.waitForText("关于VerySecret");
			solo.waitForText("退出当前账号");            
		}
	
		/*
		public void testLogOut() throws Exception{
			solo.clickOnButton("我");
			solo.clickOnButton("退出当前帐号");
			solo.clickOnButton("确定");
			solo.waitForText("快速注册");
		}
		*/
		
		@Override
		public void tearDown() throws Exception {
	
		try {
			
		this.solo.finishOpenedActivities();
	
		} catch (Throwable e) {
	
		e.printStackTrace();
		
		this.activity.finish();
	
		super.tearDown();
	
		}
	
		}
	
	}