

# We need to check if camera
# is opened previously or not


# We need to set resolutions.
# so, convert them from float to integer.


# Below VideoWriter object will create
# a frame of above defined The output
# is stored in 'filename.avi' file.

	
while(True):
	ret, frame = video.read()

	if ret == True:

		# Write the frame into the
		# file 'filename.avi'
		result.write(frame)

		# Display the frame
		# saved in the file
		cv2.imshow('Frame', frame)

		# Press S on keyboard
		# to stop the process
		if cv2.waitKey(1) & 0xFF == ord('s'):
			break

	# Break the loop
	else:
		break

# When everything done, release
# the video capture and video
# write objects
video.release()
result.release()
	
# Closes all the frames
cv2.destroyAllWindows()

print("The video was successfully saved")
