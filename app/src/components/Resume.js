import {
  Page,
  Text,
  View,
  Document,
  StyleSheet,
  Image,
} from "@react-pdf/renderer";

const styles = StyleSheet.create({
  body: {
    paddingTop: 35,
    paddingBottom: 65,
    paddingHorizontal: 35,
    fontSize: 12,
    color: "#333",
  },

  page: {
    flexDirection: "row",
    backgroundColor: "#d3d3d5",
  },

  header: {
    marginBottom: 30,
    padding: 10,
    textAlign: "center",
  },

  profile: {
    fontSize: 24,
    marginTop: 5,
  },

  title: {
    fontSize: 14,
    fontWeight: "bold",
    marginBottom: 5,
  },

  subtitle: {
    color: "#333",
  },

  desc: {
    marginTop: 10,
  },

  dates: {
    marginTop: 5,
    color: "#787880",
  },

  section: {
    marginVertical: 10,
  },

  eduSection: {
    marginBottom: 10,
  },

  sectionTitle: {
    fontSize: 18,
    fontWeight: "bold",
    marginVertical: 10,
  },

  eduTitle: {
    fontSize: 14,
  },

  image: {
    width: 150,
    height: 150,
    borderRadius: "50%",
    alignSelf: "center",
  },

  pageNumber: {
    position: "absolute",
    fontSize: 12,
    bottom: 30,
    left: 0,
    right: 0,
    textAlign: "center",
    color: "grey",
  },
});

const Resume = (data) => {
  const profileData = data.data;
  return (
    <Document>
      <Page style={styles.body}>
        <View style={styles.header} fixed>
        {profileData?.img && <Image
            style={styles.image}
            src={profileData.img}
            alt={`${profileData.name} Picture`}
          />}
          <Text style={styles.profile}>{profileData.name}</Text>
          <Text style={styles.desc}>{profileData.location}</Text>
        </View>
        <Text style={styles.sectionTitle}>Education</Text>
        {profileData.education.map((edu, i) => (
          <View style={styles.eduSection} key={`edu${i}`}>
            <Text style={styles.eduTitle}>{edu.university}</Text>
            <Text style={styles.dates}>
              {edu.degree} ({edu.dates})
            </Text>
          </View>
        ))}
        <Text style={styles.sectionTitle}>Experience</Text>
        {profileData.experience.map((exp, i) => (
          <View style={styles.section} key={`exp${i}`}>
            <Text style={styles.title}>{exp.company_name}</Text>
            <Text style={styles.subtitle}>{exp.position}</Text>
            <Text style={styles.dates}>{exp.dates}</Text>
            <Text style={styles.desc}>{exp.details}</Text>
          </View>
        ))}

        <Text
          style={styles.pageNumber}
          render={({ pageNumber, totalPages }) =>
            `${pageNumber} / ${totalPages}`
          }
          fixed
        />
      </Page>
    </Document>
  );
};

export default Resume;
